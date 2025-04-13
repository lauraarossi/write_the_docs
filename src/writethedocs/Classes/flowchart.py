import logging
import traceback
from pathlib import Path
from ..Utilities import shell


class Flowchart:
    """
    Class to configure and run pyflowchart.

    Parameters
    ----------
    source_code_path: str | Path
        Source code root directory.
    entry_file: str | Path
        Entry file name.
    flowchart_filepath: str | Path
        Path to which flowchart will be saved.

    Attributes
    ----------
    source_code_path: str | Path
        Source code root directory.
    entry_file: str | Path
        Entry file name.
    flowchart_filepath: str | Path
        Path to which flowchart will be saved.
    """

    def __init__(
        self,
        source_code_path: str | Path,
        entry_file: str | Path,
        flowchart_filepath: str | Path,
    ):
        try:
            self.logger = logging.getLogger(__name__)
            self.source_code_path = source_code_path
            self.entry_file = entry_file
            self.flowchart_filepath = flowchart_filepath
        except Exception as e:
            msg = (
                f"Error in flowchart initialisation: {traceback.format_exc()}"
            )
            self.logger.error(msg)
            raise e

    def run(self) -> None:
        """Run flake8 on PowerShell."""
        try:
            out, err, exit_code = shell(
                [
                    "powershell.exe",
                    "python",
                    " -m",
                    "pyflowchart",
                    f"{Path(self.source_code_path, self.entry_file)}",
                    "-o",
                    self.flowchart_filepath,
                ],
                self.logger,
            )
            return out, err, exit_code
        except Exception as e:
            msg = f"Error in flowchart run: {traceback.format_exc()}"
            self.logger.error(msg)
            raise e
