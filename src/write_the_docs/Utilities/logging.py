import logging
import coloredlogs
from pathlib import Path


def configure_logging(filepath: str | Path):
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
    filepath = Path(filepath)
    if not filepath.parent.exists():
        filepath.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%d/%m/%Y %I:%M:%S %p",
        handlers=[
            logging.FileHandler(filename=filepath, mode="w", encoding="ansi"),
            logging.StreamHandler(),
        ],
    )
    coloredlogs.install(level="DEBUG")
