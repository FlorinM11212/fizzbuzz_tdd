import unittest

from fizzbuzz import fizzbuzz


class FizzBuzzTests(unittest.TestCase):
    #First test.
    def test_returns_number_as_string_for_one(self):
        self.assertEqual(fizzbuzz(1), "1")
    #Second test.
    def test_returns_number_as_string_for_two(self):
        self.assertEqual(fizzbuzz(2), "2")
    #Third test.
    def test_returns_fizz_for_three(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
    #Fourth test.
    def test_returns_fizz_for_six(self):
        self.assertEqual(fizzbuzz(6), "Fizz")
    #Fifth test.
    def test_returns_buzz_for_five(self):
        self.assertEqual(fizzbuzz(5), "Buzz")
    #Sext test.
    def test_returns_buzz_for_ten(self):
        self.assertEqual(fizzbuzz(10), "Buzz")
    #Seventh test.
    def test_returns_fizzbuzz_for_fifteen(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
    # Eighth test.
    def test_returns_fizzbuzz_for_thirty(self):
        self.assertEqual(fizzbuzz(30), "FizzBuzz")
    #Nineth test.
    def test_full_sequence_first_fifteen(self):

        #Expected return. 
        expected = [
            "1", "2", "Fizz", "4", "Buzz",
            "Fizz", "7", "8", "Fizz", "Buzz",
            "11", "Fizz", "13", "14", "FizzBuzz",
        ]
        self.assertEqual([fizzbuzz(i) for i in range(1, 16)], expected)


if __name__ == "__main__":
    unittest.main()
