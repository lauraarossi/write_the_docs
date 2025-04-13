import typer
from typing_extensions import Annotated
import traceback
import logging
from pathlib import Path
from writethedocs.Utilities import (
    configure_logging,
    set_permissions,
    str_to_html,
)
from Classes import Black, Flake8, Flowchart, Sphinx, UnitTests


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
    author: Annotated[
        str,
        typer.Argument(
            help=r"""Author name and/or email, e.g. Padmini Johnson, pjohnson@example.com."""
        ),
    ],
    version: Annotated[
        str,
        typer.Argument(
            help=r"""Version of code being documented, e.g. 1.0.2"""
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
        typer.Argument(
            help=r"""Optional line length for black formatter and flake8."""
        ),
    ] = 79,
    logs_output_dir: Annotated[
        str,
        typer.Argument(
            help=r"""Optional directory, where logs will be saved to."""
        ),
    ] = "Logs",
    logs_flowchart_dir: Annotated[
        str,
        typer.Argument(
            help=r"""Optional directory, where flowchart will be saved to."""
        ),
    ] = "Flowchart",
    docs_outputs_dir: Annotated[
        str,
        typer.Argument(
            help=r"""Optional directory, where docs will be saved to."""
        ),
    ] = "Docs",
    pytest_html_path: Annotated[
        str,
        typer.Argument(
            help=r"""Optional directory, where docs will be saved to."""
        ),
    ] = "UnitTests",
    coverage_html_path: Annotated[
        str,
        typer.Argument(
            help=r"""Optional directory, where docs will be saved to."""
        ),
    ] = "Coverage",
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
    log_dir = Path(source_code_path, logs_output_dir, "log.log")
    configure_logging(log_dir)
    logger = logging.getLogger(__name__)
    logger.info("Starting.")
    try:

        set_permissions(logger)

        logger.info("Running black.")
        Black(source_code_path, line_length).run()

        logger.info("Running flake8.")
        Flake8(source_code_path, line_length).run()

        logger.info("Running pyflowchart.")
        flowchart_filepath = Path(
            source_code_path, logs_flowchart_dir, "flowchart.html"
        )
        Path(Path.cwd(), flowchart_filepath).parent.mkdir(
            parents=True, exist_ok=True
        )
        Flowchart(source_code_path, entry_file, flowchart_filepath).run()

        logger.info("Running Sphinx.")
        Sphinx(
            source_code_path,
            project_name,
            author,
            version,
            release,
            docs_outputs_dir,
        ).run()

        # save pre-test logger
        with open(Path(log_dir), "r") as file:
            pre_test_log = file.read()

        logger.info("Running UnitTests and Coverage.")
        pytest_html = Path(source_code_path, pytest_html_path)
        pytest_html.parent.mkdir(parents=True, exist_ok=True)
        coverage_html = Path(source_code_path, coverage_html_path)
        coverage_html.parent.mkdir(parents=True, exist_ok=True)
        UnitTests(
            source_code_path,
            pytest_html,
            coverage_html,
        ).run_coverage()

        logger.info("All done!")

        # post-test logger
        with open(Path(log_dir), "r") as file:
            post_test_log = file.read()

        full_log = pre_test_log + post_test_log
        str_to_html(
            full_log,
            Path(source_code_path, logs_output_dir, "log.html"),
            logger,
        )

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
