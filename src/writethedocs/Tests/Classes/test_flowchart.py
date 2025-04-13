import unittest
import shutil
from pathlib import Path
from ...Classes import Flowchart


temp_path = Path(Path(__file__).parent.parent, "temp", "Flowchart")
temp_path.mkdir(exist_ok=True, parents=True)
correct_init = Flowchart(".", "main.py", temp_path)


class TestFlowchart(unittest.TestCase):

    def test_flowchart_init(self):
        """Test initialisation of flowchart class."""
        f = correct_init
        assert f.source_code_path == "."
        assert f.entry_file == "main.py"
        assert f.flowchart_filepath == temp_path

    # def test_flowchart_run(self):
    #     """Test running flowchart."""
    #     out, err, exit_code = correct_init.run()
    #     assert isinstance(out, str)
    #     assert isinstance(err, str)
    #     assert isinstance(exit_code, int)

    def test_flowchart_fail_init(self):
        """Test initialisation of flowchart fails with missing paramters."""
        with self.assertRaises(Exception):
            Flowchart()

    def test_flowchart_fail_run(self):
        """Test running flowchart fails with missextraing paramters."""
        with self.assertRaises(Exception):
            correct_init.run(54)


if __name__ == "__main__":
    unittest.main()
