import typer
from typing_extensions import Annotated
import traceback
import logging
from pathlib import Path
from ansi2html import Ansi2HTMLConverter
from write_the_docs.Utilities import configure_logging, shell


def run_all(
    source_code_path: Annotated[
        str,
        typer.Argument(
            help=r"""Path to root directory of the code you want to document, e.g. C:\Users\you\MyAwesomeApp\src"""
        ),
    ],
    entry_file: Annotated[
        str,
        typer.Argument(
            help=r"""Entry script to the code, e.g. main.py. This is the code that will be flowcharted."""
        ),
    ],
    project_name: Annotated[
        str,
        typer.Argument(
            help=r"""Name of the project to include in the documentation, e.g. My Awesome App"""
        ),
    ],
    version: Annotated[
        str,
        typer.Argument(
            help=r"""Version of code being documented, e.g. 1.0.2"""
        ),
    ],
    author: Annotated[
        str,
        typer.Argument(
            help=r"""Author name and/or email, e.g. Padmini Johnson, pjohnson@example.com."""
        ),
    ],
    release: Annotated[
        str,
        typer.Argument(
            help=r"""Name of the release version, e.g. initial release, e.g. 1/5/1875"""
        ),
    ],
    line_length: Annotated[
        int,
        typer.Option(
            help=r"""Optional line length for black formatter and flake8."""
        ),
    ] = 79,
    logs_output_dir: Annotated[
        str,
        typer.Option(
            help=r"""Optional directory, where logs will be saved to."""
        ),
    ] = "Logs",
    logs_flowchart_dir: Annotated[
        str,
        typer.Option(
            help=r"""Optional directory, where flowchart will be saved to."""
        ),
    ] = "Flowchart",
    logs_docs_dir: Annotated[
        str,
        typer.Option(
            help=r"""Optional directory, where docs will be saved to."""
        ),
    ] = "Docs",
):
    """
    Main call for the application.
    Orchestrates calls to all other modules, executing from top to bottom.

    Parameters
    ----------
    source_code_path: str
        Path to root directory of code to document.
    entry_file: str
        Entry script to the code, e.g. main.py
    project_name: str
        Name for the project.
    version: str
        Version of code being documented.
    author: str
        Author name and/or email.
    release: str
        Release version.
    line_length: int = 79
        Optional line length for black formatter and flake8.
    logs_output_dir: str = Logs
        Optional directory, where logs will be saved to.
    logs_flowchart_dir: str = Logs
        Optional directory, where flowchart will be saved to.
    """
    logger = logging.getLogger(__name__)
    try:
        log_dir = f"{logs_output_dir}/log.log"
        configure_logging(log_dir)
        logger = logging.getLogger(__name__)
        logger.info("Starting.")

        shell(
            [
                "powershell.exe",
                "Set-ExecutionPolicy",
                "-Scope",
                "CurrentUser",
                "RemoteSigned",
            ],
            logger,
        )

        logger.info("Running black.")
        shell(
            [
                "powershell.exe",
                "black",
                f"{source_code_path}",
                "--line-length",
                f"{line_length}",
            ],
            logger,
            False,
        )

        logger.info("Running flake8.")
        shell(
            [
                "powershell.exe",
                "flake8",
                f"--max-line-length={line_length}",
                "--per-file-ignores='__init__.py:F401'",
                f"{source_code_path}",
            ],
            logger,
            False,
        )

        logger.info("Running pyflowchart.")
        flowchart_filepath = f"{logs_flowchart_dir}/flowchart.html"
        Path(Path.cwd(), flowchart_filepath).parent.mkdir(
            parents=True, exist_ok=True
        )

        shell(
            [
                "powershell.exe",
                "python",
                " -m",
                "pyflowchart",
                f"{Path(source_code_path, entry_file)}",
                "-o",
                flowchart_filepath,
            ],
            logger,
        )

        logger.info("Running Sphinx.")
        shell(
            [
                "powershell.exe",
                "./Sphinx.ps1",
                "-Path",
                f"{source_code_path}",
                "-Project",
                f"{project_name}",
                "-Author",
                f"{author}",
                "-Version",
                f"{version}",
                "-Release",
                f"{release}",
                "-OutputDir",
                f"{logs_docs_dir}",
            ],
            logger,
        )

        logger.info("Converting logs to html.")
        with open(Path(Path.cwd(), log_dir), "r") as file:
            lines = file.read()

        converter = Ansi2HTMLConverter(title="Log")
        html_string = converter.convert(lines)

        with open(f"{logs_output_dir}/log.html", "w") as file:
            file.write(html_string)

        logger.info("All done!")

    except Exception as e:
        msg = f"Error in run_all: {traceback.format_exc()}"
        logger.error(msg)
        raise e


try:
    app = typer.Typer()
    app.command()(run_all)

except Exception as e:
    msg = f"Error in main call: {traceback.format_exc()}"
    print(msg)
    raise e

if __name__ == "__main__":
    app()
