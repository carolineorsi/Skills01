import unittest
from list_comps2 import *

class TestSkillsFunctions(unittest.TestCase):

	def setUp(self):
		self.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		self.words = ["hello", "my", "name", "is", "Buster", "Posey"]

	def test_all_odd(self):
		self.assertEqual(all_odd(self.numbers), [1, 3, 5, 7, 9])

	def test_all_even(self):
		self.assertEqual(all_even(self.numbers), [2, 4, 6, 8])

	def test_long_words(self):
		self.assertEqual(long_words(self.words), ["hello", "name", "Buster", "Posey"])

if __name__ == '__main__':
    unittest.main()