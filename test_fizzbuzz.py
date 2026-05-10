import unittest

from fizzbuzz import fizzbuzz


class FizzBuzzTests(unittest.TestCase):
    def test_returns_number_as_string_for_one(self):
        self.assertEqual(fizzbuzz(1), "1")

    def test_returns_number_as_string_for_two(self):
        self.assertEqual(fizzbuzz(2), "2")

    def test_returns_fizz_for_three(self):
        self.assertEqual(fizzbuzz(3), "Fizz")

    def test_returns_fizz_for_six(self):
        self.assertEqual(fizzbuzz(6), "Fizz")


if __name__ == "__main__":
    unittest.main()
