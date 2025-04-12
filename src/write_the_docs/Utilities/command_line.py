from subprocess import run, Popen, PIPE, CompletedProcess
import logging
import traceback


def run_command(cmd: str, logger: logging.Logger) -> CompletedProcess[bytes]:
    """
    Runs a powershell command.
    """
    try:
        completed = run(["powershell", "-Command", cmd], capture_output=True)
        return completed

    except Exception as e:
        msg = f"Error in run_command call: {traceback.format_exc()}"
        logger.error(msg)
        raise e


def shell(args: list[str], logger: logging.Logger, raise_err: bool = True):
    """
    Calls subprocess.Popen pipes to call out to the shell.

    Parameters
    ----------
    args: list[str]
        args to the command
    logger: logging.Logger
        Logger.
    raise_err: bool
        Log error and raise exception if anything is passed to stderr.
        Default true. If False, err will be logged as a warning instead,
        and no exception raised.

    Returns
    -------
    out: str
        Decoded stdout.
    err: str
        Decoded stderr.
    """
    try:
        p = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=False)
        stdout, stderr = p.communicate()
        out = stdout.decode("utf-8")
        err = stderr.decode("utf-8")
        exit_code = p.returncode

        if exit_code != 0:
            msg = f"Exit code for {args} is: {exit_code}. \n {out} \n {err}"
            if raise_err:
                logger.error(msg)
                raise Exception(msg)
            else:
                logger.warning(msg)
        elif out:
            logger.info(out)

        return out, err, p.returncode

    except Exception as e:
        msg = f"Error in shell call: {traceback.format_exc()}"
        logger.error(msg)
        raise e
