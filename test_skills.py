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

	def test_halvesies(self):
		self.assertEqual(halvesies(self.numbers), [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5])
		self.assertEqual(halvesies(self.numbers2), [2.0, 4.0, 1.5, 0.0, 7.0, -1.0])

	def test_word_lengths(self):
		self.assertEqual(word_lengths(self.words), [5, 2, 4, 2, 6, 5])

	def test_sum_numbers(self):
		self.assertEqual(sum_numbers(self.numbers), 45)
		self.assertEqual(sum_numbers(self.numbers2), 27)

	def test_mult_numbers(self):
		self.assertEqual(mult_numbers(self.numbers), 362880)
		self.assertEqual(mult_numbers(self.numbers2), 0)

	def test_join_strings(self):
		self.assertEqual(join_strings(self.words), "hello my name is Buster Posey")

	def test_average(self):
		self.assertEqual(average(self.numbers), 5.0)
		self.assertEqual(average(self.numbers2), 4.5)

if __name__ == '__main__':
    unittest.main()