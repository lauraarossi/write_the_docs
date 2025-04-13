import logging
import traceback
from pathlib import Path
from write_the_docs.Utilities import shell


class Black:
    """
    Class to configure and run black formatter.

    Parameters
    ----------
    source_code_path: str | Path
        Source code root directory.
    line_length: int
        Line length to pass to black formatter as line-length.
    additional_params: list[str]
        Optional additional paramters for Sphinx autodoc.

    Attributes
    ----------
    source_code_path: str | Path
        Source code root directory.
    line_length: int
        Line length to pass to black formatter as line-length.
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
            msg = f"Error in black initialisation: {traceback.format_exc()}"
            self.logger.error(msg)
            raise e

    def run(self) -> None:
        """Run black on PowerShell."""
        try:
            out, err, exit_code = shell(
                [
                    "powershell.exe",
                    "black",
                    f"{self.source_code_path}",
                    "--line-length",
                    f"{self.line_length}",
                ],
                self.logger,
                False,
                *self.additional_params,
            )
            return out, err, exit_code
        except Exception as e:
            msg = f"Error in black run: {traceback.format_exc()}"
            self.logger.error(msg)
            raise e
