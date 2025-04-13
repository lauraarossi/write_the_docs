import unittest
from pathlib import Path
from ...Classes import UnitTests

temp_path = Path(Path(__file__).parent.parent, "temp", "Docs")
temp_path.mkdir(exist_ok=True, parents=True)

correct_init = UnitTests("Tests/Utilities", "UnitTests", "Coverage")


class TestUnitTests(unittest.TestCase):

    def test_unit_tests_init(self):
        """Test initialisation of unit_tests class."""
        ut = correct_init
        assert ut.pytest_html_path == "UnitTests"
        assert ut.coverage_html_path == "Coverage"

    def test_unit_tests_fail_init(self):
        """Test initialisation of unit_tests fails with missing parameters."""
        with self.assertRaises(Exception):
            UnitTests()

    def test_unit_tests_fail_run_tests(self):
        """Test running of unit_tests.run_tests fails with extra parameters."""
        with self.assertRaises(Exception):
            correct_init.run_tests(1)

    def test_unit_tests_fail_run_coverage(self):
        """Test running of unit_tests.run_coverage fails with extra parameters."""
        with self.assertRaises(Exception):
            correct_init.run_coverage(1)


if __name__ == "__main__":
    unittest.main()
