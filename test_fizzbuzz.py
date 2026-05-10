import unittest

from fizzbuzz import fizzbuzz


class FizzBuzzTests(unittest.TestCase):
    def test_returns_number_as_string_for_one(self):
        self.assertEqual(fizzbuzz(1), "1")


if __name__ == "__main__":
    unittest.main()
