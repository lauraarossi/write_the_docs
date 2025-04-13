import logging
import traceback
from pathlib import Path
from write_the_docs.Utilities import shell


class Flake8:
    """
    Class to configure and run flake8.

    Parameters
    ----------
    source_code_path: str | Path
        Source code root directory.
    entry_file: str | Path
        Line length to pass to flake8 as max-line-length.
    additional_params: list[str]
        Optional additional paramters for Sphinx autodoc.

    Attributes
    ----------
    source_code_path: str | Path
        Source code root directory.
    line_length: int
        Line length to pass to flake8 as max-line-length.
    logger: Logger
        Logger to pass messages to.
    additional_params: list[str]
        Optional additional paramters for Sphinx autodoc.
    """

    def __init__(
        self,
        source_code_path: str | Path,
        line_length: int,
        additional_params: list[str] = list(),
    ):
        try:
            self.logger = logging.getLogger(__name__)
            self.source_code_path = source_code_path
            self.line_length = line_length
            self.additional_params = additional_params

        except Exception as e:
            msg = f"Error in flake8 initialisation: {traceback.format_exc()}"
            self.logger.error(msg)
            raise e

    def run(self) -> None:
        """Run flake8 on PowerShell."""
        try:
            out, err, exit_code = shell(
                [
                    "powershell.exe",
                    "flake8",
                    f"--max-line-length={self.line_length}",
                    "--per-file-ignores='__init__.py:F401'",
                    f"{self.source_code_path}",
                    *self.additional_params,
                ],
                self.logger,
                False,
            )
            return out, err, exit_code

        except Exception as e:
            msg = f"Error in flake8 run: {traceback.format_exc()}"
            self.logger.error(msg)
            raise e
