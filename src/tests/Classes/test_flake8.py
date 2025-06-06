import unittest
from writethedocs.Classes import Flake8

correct_init = Flake8(
    ".",
    79,
)


class TestFlake8(unittest.TestCase):

    def test_flake8_init(self):
        """Test initialisation of Flake8 class."""
        f = correct_init
        assert f.source_code_path == "."
        assert f.line_length == 79
        assert f.additional_params == list()

    def test_flake8_fail_init(self):
        """Test initialisation of Flake8 fails with missing paramters."""
        with self.assertRaises(Exception):
            f = Flake8()

    def test_flake8_fail_run(self):
        """Test running Flake8 fails with extra paramters."""
        with self.assertRaises(Exception):
            f = correct_init.run("apple")


if __name__ == "__main__":
    unittest.main()
