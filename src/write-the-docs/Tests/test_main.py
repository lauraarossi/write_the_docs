import unittest
from pathlib import Path
from write_the_docs import run_all, app
import shutil

temp_path = Path("Tests", "temp")


class TestMain(unittest.TestCase):

    def test_app_missing_params(self):
        """Test failure if parameters not given."""
        with self.assertRaises(TypeError):
            run_all()  # parameters missing

    def test_app_incorrect_params(self):
        """Test failure if parameters are the wrong type."""
        with self.assertRaises(TypeError):
            run_all(5, 6, 7, 8, 9, 10)  # parameters wrong type

    def test_app_path_does_not_exist(self):
        """Test failure if parameters point to non-existent path."""
        with self.assertRaises(Exception):
            run_all(
                "/fake/path",
                "main.py",
                "Write The Docs",
                "1.0.0",
                "LAR",
                "Q1",
                79,
                Path(temp_path, "Logs"),
                Path(temp_path, "Flowchart"),
                Path(temp_path, "Docs"),
            )  # parameters wrong type


if __name__ == "__main__":
    unittest.main()
