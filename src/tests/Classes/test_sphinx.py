import unittest
from pathlib import Path
from writethedocs.Classes import Sphinx

temp_path = Path(Path(__file__).parent.parent, "temp", "Docs")
temp_path.mkdir(exist_ok=True, parents=True)

correct_init = Sphinx(
    ".",
    "Write The Docs",
    "LAR",
    "1.0.0",
    "Q1",
    temp_path,
)


class TestSphinx(unittest.TestCase):

    def test_sphinx_init(self):
        """Test initialisation of sphinx class."""
        s = correct_init
        assert s.source_code_path == "."
        assert s.project_name == "Write The Docs"
        assert s.author == "LAR"
        assert s.version == "1.0.0"
        assert s.release == "Q1"
        assert s.docs_outputs_dir == temp_path
        assert s.additional_params == list()

    def test_sphinx_run(self):
        """Test running sphinx."""
        out, err, exit_code = correct_init.run()
        assert isinstance(out, str)
        assert isinstance(err, str)
        assert isinstance(exit_code, int)

    def test_sphinx_fail_init(self):
        """Test initialisation of sphinx fails with missing parameters."""
        with self.assertRaises(Exception):
            Sphinx()

    def test_sphinx_fail_run(self):
        """Test running of sphinx fails with extra parameters."""
        with self.assertRaises(Exception):
            correct_init.run(1)


if __name__ == "__main__":
    unittest.main()
