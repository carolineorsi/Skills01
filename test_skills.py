import unittest
from list_comps2 import *

class TestSkillsFunctions(unittest.TestCase):

	def setUp(self):
		self.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		self.numbers2 = [4, 8, 3, 0, 14, -2]
		self.words = ["hello", "my", "name", "is", "Buster", "Posey"]

	def test_all_odd(self):
		self.assertEqual(all_odd(self.numbers), [1, 3, 5, 7, 9])
		self.assertEqual(all_odd(self.numbers2), [3])

	def test_all_even(self):
		self.assertEqual(all_even(self.numbers), [2, 4, 6, 8])
		self.assertEqual(all_even(self.numbers2), [4, 8, 0, 14, -2])

	def test_long_words(self):
		self.assertEqual(long_words(self.words), ["hello", "name", "Buster", "Posey"])

	def test_smallest(self):
		self.assertEqual(smallest(self.numbers), 1)
		self.assertEqual(smallest(self.numbers2), -2)

	def test_largest(self):
		self.assertEqual(largest(self.numbers), 9)
		self.assertEqual(largest(self.numbers2), 14)

if __name__ == '__main__':
    unittest.main()