import unittest
from pathlib import Path
import logging
from writethedocs.Utilities import set_permissions, shell
from writethedocs.Classes import Sphinx

temp_path = Path(Path(__file__).parent.parent, "temp", "Docs")
temp_path.mkdir(exist_ok=True, parents=True)
logger = logging.getLogger()


class TestCommandLine(unittest.TestCase):

    def test_set_permissions(self):
        """Test set_permissions runs as expected."""
        set_permissions(logger)
        out, err, exit_code = Sphinx(
            ".",
            "Write The Docs",
            "LAR",
            "1.0.0",
            "Q1",
            temp_path,
        ).run()
        assert isinstance(out, str)
        assert isinstance(err, str)
        assert isinstance(exit_code, int)
        assert exit_code == 0

    def test_configure_logging_fails(self):
        """Test set_permissions fails with wrong imputs."""
        with self.assertRaises(TypeError):
            set_permissions()

    def test_shell(self):
        """Test shell runs as expected."""
        out, err, exit_code = shell(["cmd", "ls"], logger)
        assert isinstance(out, str)
        assert isinstance(err, str)
        assert isinstance(exit_code, int)

    def test_shell_fail(self):
        """Test shell fails if given wrong command."""
        with self.assertRaises(TypeError):
            shell("NONESENSE")


if __name__ == "__main__":
    unittest.main()
