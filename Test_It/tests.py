"""
Jacob Rammer
Writing test functions
"""
"""Unit tests for testme.py"""

import unittest
from buggy import *


class TestMaxRun(unittest.TestCase):

    def test_max_run_example(self):
        self.assertEqual(max_run([1, 2, 2, 2, 3]), [2, 2, 2])

    def test_max_run_empty(self):  # finds bug #1
        self.assertEqual(max_run([]), [])

    def test_max_run_single(self):  # finds bug #2
        self.assertEqual(max_run([1]), [1])

    def test_max_run_mixed(self):
        self.assertEqual(max_run(["a", "A", 1, 3]), ["a"])
        self.assertEqual(max_run([1, "1"]), [1])
        self.assertEqual(max_run(["1", 1]), ["1"])

    def test_max_run_string(self):
        self.assertEqual(max_run(["Testing"]), ["Testing"])  # #1
        self.assertEqual(max_run(["Testing", ["123"]]), ["123"])




if __name__ == "__main__":
    unittest.main()
