import unittest
from writethedocs.Classes import Black

correct_init = Black(".", 79)


class TestBlack(unittest.TestCase):

    def test_black_init(self):
        """Test initialisation of black class."""
        b = correct_init
        assert b.source_code_path == "."
        assert b.line_length == 79
        assert b.additional_params == list()

    def test_black_run(self):
        """Test running black."""
        out, err, exit_code = correct_init.run()
        assert isinstance(out, str)
        assert isinstance(err, str)
        assert isinstance(exit_code, int)

    def test_black_fail_init(self):
        """Test initialisation of black fails with missing paramters."""
        with self.assertRaises(Exception):
            Black()

    def test_black_fail_run(self):
        """Test running black fails with extra paramters."""
        with self.assertRaises(Exception):
            correct_init.run(65)


if __name__ == "__main__":
    unittest.main()
