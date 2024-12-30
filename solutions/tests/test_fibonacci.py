"""This module runs the test for the fibonacci function."""

import unittest

from solutions.fibonacci import fibonacci


class TestFibonacci(unittest.TestCase):
    """Test cases for the fibonacci function."""

    def test_valid_inputs(self):
        """Test fibonacci function with valid inputs."""
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci(1), [0])
        self.assertEqual(fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
        self.assertEqual(fibonacci(4), [0, 1, 1, 2])

    def test_invalid_inputs(self):
        """Test fibonacci function with invalid inputs."""
        with self.assertRaises(ValueError):
            fibonacci(-1)  # Negative input

        with self.assertRaises(ValueError):
            fibonacci("a")  # String input

        with self.assertRaises(ValueError):
            fibonacci(3.5)  # Float input

        with self.assertRaises(ValueError):
            fibonacci([])  # List input


if __name__ == "__main__":
    unittest.main()
