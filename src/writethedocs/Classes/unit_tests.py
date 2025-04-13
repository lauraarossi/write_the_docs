import logging
import traceback
from pathlib import Path
from ..Utilities import shell


class UnitTests:
    """
    Class to configure and run pytest and coverage.

    Parameters
    ----------
    source_code_path: str | Path
        Source code root directory.
    pytest_html_path: str | Path
        Directory for pytest html report.
    coverage_html_path: str | Path
        Directory for coverage html report.

    Attributes
    ----------
    source_code_path: str | Path
        Source code root directory.
    pytest_html_path: str | Path
        Directory for pytest html report.
    coverage_html_path: str | Path
        Directory for coverage html report.
    logger: logging.Logger
        Logger to write to during execution.
    """

    def __init__(
        self,
        source_code_path: str | Path,
        pytest_html_path: str | Path,
        coverage_html_path: str | Path,
    ):
        try:
            self.logger = logging.getLogger(__name__)
            self.source_code_path = source_code_path
            self.pytest_html_path = pytest_html_path
            self.coverage_html_path = coverage_html_path

        except Exception as e:
            msg = f"Error in tests initialisation: {traceback.format_exc()}"
            self.logger.error(msg)
            raise e

    def run_tests(self) -> None:
        """Run tests on PowerShell."""
        try:
            out, err, exit_code = shell(
                [
                    "powershell.exe",
                    "coverage",
                    "run",
                    "--data-file",
                    f"{self.source_code_path}/.coverage",
                    "-m",
                    "pytest",
                    "-v",
                    f"{self.source_code_path}",
                    f"--html-report={self.pytest_html_path}",
                ],
                self.logger,
            )
            return out, err, exit_code
        except Exception as e:
            msg = f"Error in tests run_tests: {traceback.format_exc()}"
            self.logger.error(msg)
            raise e

    def run_coverage(self) -> None:
        """Run tests on PowerShell."""
        try:
            self.logger.info("Running tests and report.")
            self.run_tests()  # must run first
            self.logger.info("Running coverage report.")
            out, err, exit_code = shell(
                [
                    "powershell.exe",
                    "coverage",
                    "html",
                    "-d",
                    f"{self.coverage_html_path}",
                    "--skip-empty",
                    f"--data-file={self.source_code_path}/.coverage",
                ],
                self.logger,
            )
            return out, err, exit_code
        except Exception as e:
            msg = f"Error in tests run_coverage: {traceback.format_exc()}"
            self.logger.error(msg)
            raise e
