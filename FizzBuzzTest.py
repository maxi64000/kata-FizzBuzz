import unittest

from main import FizzBuzz

class FizzBuzzTest(unittest.TestCase):

    def test_ShouldReturn_TheNumber(self):
        self.assertEqual(FizzBuzz(0), 0)

    def test_ShouldReturn_Fizz_WithTheNumberThree(self):
        self.assertEqual(FizzBuzz(3), "Fizz")

    def test_ShouldReturn_Fizz_WithMultipleOfThree(self):
        self.assertEqual(FizzBuzz(6), "Fizz")

    def test_ShouldReturn_Buzz_WithTheNumberFive(self):
        self.assertEqual(FizzBuzz(5), "Buzz")

    def test_ShouldReturn_Buzz_WithMultipleOfFive(self):
        self.assertEqual(FizzBuzz(10), "Buzz")

    def test_ShouldReturn_FizzBuzz_WithMultipleOfThree_And_WithMultipleOfFive(self):
        self.assertEqual(FizzBuzz(15), "FizzBuzz")

if __name__ == '__main__':
    unittest.main()