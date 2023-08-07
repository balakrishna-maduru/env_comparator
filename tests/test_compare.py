import json
import unittest
from env_comparator.compare import Compare


class TestCompare(unittest.TestCase):

    def read_json(self, file):
        with open(file) as f:
            return json.load(f)

    def test_compare_equal(self):
        file1 = "resources/requirements_env1.txt"
        file2 = "resources/requirements_env1_same.txt"
        compare = Compare(file1, file2)
        self.assertEqual(compare.get_results(), self.read_json(
            "resources/test_compare_equal.json"))

    def test_compare_version_diff(self):
        file1 = "resources/requirements_env1.txt"
        file2 = "resources/requirements_env2.txt"
        compare = Compare(file1, file2)
        self.assertEqual(compare.get_results(), self.read_json(
            "resources/test_compare_equal_version_diff.json"))

    def test_compare_file1_diff(self):
        file1 = "resources/requirements_env1.txt"
        file2 = "resources/requirements_env3.txt"
        compare = Compare(file1, file2)
        self.assertEqual(compare.get_results(), self.read_json(
            "resources/test_compare_equal_file1_diff.json"))

    def test_compare_file2_diff(self):
        file1 = "resources/requirements_env3.txt"
        file2 = "resources/requirements_env1.txt"
        compare = Compare(file1, file2)
        self.assertEqual(compare.get_results(), self.read_json(
            "resources/test_compare_equal_file2_diff.json"))

    def test_compare_subset_false(self):
        file1 = "resources/requirements_env3.txt"
        file2 = "resources/requirements_env1.txt"
        compare = Compare(file1, file2)
        self.assertEqual(compare.is_subset(), False)

    def test_compare_subset_true(self):
        file1 = "resources/requirements_env1.txt"
        file2 = "resources/requirements_env3.txt"
        compare = Compare(file1, file2)
        self.assertEqual(compare.is_subset(), True)
