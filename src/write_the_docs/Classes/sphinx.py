import logging
import traceback
from pathlib import Path
from write_the_docs.Utilities import shell


class Sphinx:
    """
    Class to configure and run sphinx.

    Parameters
    ----------
    source_code_path: str | Path
        Source code root directory.
    project_name: str
        Name of project being documented.
    author: str
        Name/email of project Author(s), as a single string.
    version: str
        Version of project being documented.
    release: str
        Release of project being documented.
    docs_outputs_dir: str | Path
        Location for docs to be saved to.
    additional_params: list[str]
        Optional additional paramters for Sphinx autodoc.

    Attributes
    ----------
    source_code_path: str | Path
        Source code root directory.
    project_name: str
        Name of project being documented.
    author: str
        Name/email of project Author(s), as a single string.
    version: str
        Version of project being documented.
    release: str
        Release of project being documented.
    docs_outputs_dir: str | Path
        Location for docs to be saved to.
    logger: Logger
        Logger to pass messages to.
    additional_params: list[str]
        Optional additional paramters for Sphinx autodoc.
    """

    def __init__(
        self,
        source_code_path: str | Path,
        project_name: str,
        author: str,
        version: str,
        release: str,
        docs_outputs_dir: str | Path,
        additional_params: list[str] = list(),
    ):
        try:
            self.logger = logging.getLogger(__name__)
            self.source_code_path = source_code_path
            self.project_name = project_name
            self.author = author
            self.version = version
            self.release = release
            self.docs_outputs_dir = docs_outputs_dir
            self.additional_params = additional_params
        except Exception as e:
            msg = f"Error in sphinx initialisation: {traceback.format_exc()}"
            self.logger.error(msg)
            raise e

    def run(self) -> None:
        """Run sphinx on PowerShell."""
        try:
            out, err, exit_code = shell(
                [
                    "powershell.exe",
                    f"{Path(__file__).parent}/Sphinx.ps1",
                    "-Path",
                    f"{self.source_code_path}",
                    "-Project",
                    f"{self.project_name}",
                    "-Author",
                    f"{self.author}",
                    "-Version",
                    f"{self.version}",
                    "-Release",
                    f"{self.release}",
                    "-OutputDir",
                    f"{self.docs_outputs_dir}",
                    *self.additional_params,
                ],
                self.logger,
            )
            return out, err, exit_code
        except Exception as e:
            msg = f"Error in sphinx run: {traceback.format_exc()}"
            self.logger.error(msg)
            raise e
