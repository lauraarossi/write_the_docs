import unittest
from pathlib import Path
import logging
from writethedocs.Utilities import set_permissions, shell
from writethedocs.Classes import Sphinx

temp_path = Path(Path(__file__).parent.parent, "temp", "Docs")
temp_path.mkdir(exist_ok=True, parents=True)
logger = logging.getLogger()


class TestCommandLine(unittest.TestCase):

    def test_configure_logging_fails(self):
        """Test set_permissions fails with wrong imputs."""
        with self.assertRaises(TypeError):
            set_permissions()

    def test_shell_fail(self):
        """Test shell fails if given wrong command."""
        with self.assertRaises(TypeError):
            shell("NONESENSE")


if __name__ == "__main__":
    unittest.main()
