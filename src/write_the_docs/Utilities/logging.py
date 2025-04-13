import logging
import coloredlogs
import traceback
from pathlib import Path
from ansi2html import Ansi2HTMLConverter


def configure_logging(filepath: str | Path) -> None:
    """
    Configure logging.
    Takes care of:
    - Format
    - File handler
    - Stream handler (stdout)

    Parameters
    ----------
    filepath: str
        Infdicates where to save the log file.
        Passed to file handler.

    Returns
    -------
    Nothing
    """
    try:
        filepath = Path(filepath)
        if not filepath.parent.exists():
            filepath.parent.mkdir(parents=True, exist_ok=True)
        logging.basicConfig(
            level=logging.DEBUG,
            handlers=[
                logging.FileHandler(
                    filename=filepath, mode="w", encoding="ansi"
                ),
                logging.StreamHandler(),
            ],
        )
        coloredlogs.install(level="DEBUG")
    except Exception as e:
        msg = f"Error in logs_to_html: {traceback.format_exc()}"
        print(msg)
        raise e


def str_to_html(input_str: str, log_output_dir: str | Path, logger) -> str:
    """
    Convert a string of raw logs to html.

    Parameters
    ----------
    input_str: str
        Raw input log.
    log_output_dir: str
        html output location.
    logger: str
        Logger to write to.

    Returns
    -------
    html_string: str
        The html formatted string.
    """
    try:
        converter = Ansi2HTMLConverter(title="Log")
        html_string = converter.convert(input_str)
        with open(log_output_dir, "w") as file:
            file.write(html_string)
        return html_string
    except Exception as e:
        msg = f"Error in logs_to_html: {traceback.format_exc()}"
        logger.error(msg)
        raise e
