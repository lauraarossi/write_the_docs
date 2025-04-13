import unittest
import logging
from pathlib import Path
from writethedocs.Utilities import str_to_html, configure_logging

temp_path = Path(Path(__file__).parent.parent, "temp", "logs")
temp_path.mkdir(exist_ok=True, parents=True)
configure_logging(Path(temp_path, "log.log"))
logger = logging.getLogger()


class TestLogging(unittest.TestCase):

    def test_configure_logging(self):
        """Test configure_logging runs as expected."""
        print(logger.handlers)
        assert isinstance(logger.handlers[0], logging.StreamHandler)
        assert isinstance(logger.handlers[2], logging.FileHandler)

    def test_configure_logging_fails(self):
        """Test configure_logging fails with wrong imputs."""
        with self.assertRaises(Exception):
            configure_logging()

    def test_str_to_html(self):
        """Test str_to_html runs as expected."""
        s = str_to_html(
            "A string \n And another", Path(temp_path, "log.html"), logger
        )
        print(s)
        assert isinstance(s, str)
        assert "</body>" in s

    def test_str_to_html_fails(self):
        """Test configure_logging fails with wrong imputs."""
        with self.assertRaises(Exception):
            str_to_html(56, Path(temp_path, "log.html"), logger)


if __name__ == "__main__":
    unittest.main()
