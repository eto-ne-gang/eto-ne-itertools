"""Test functions from the 'eto_ne_itertools' module using unittest."""


import unittest
from eto_ne_itertools import (count, cycle, combinations, combinations_with_replacement,
                              repeat, product, permutations)


class TestCount(unittest.TestCase):

    def test_type(self):
        zero_counter = count(2, 4)

        self.assertEqual(str(type(zero_counter)), '<class \'generator\'>')

    def test_step(self):
        second_counter = count(1, 5)

        self.assertEqual(next(second_counter), 1)
        self.assertEqual(next(second_counter), 6)
        self.assertEqual(next(second_counter), 11)

    def test_empty(self):
        third_counter = count()

        self.assertEqual(next(third_counter), 0)
        self.assertEqual(next(third_counter), 1)


class TestCycle(unittest.TestCase):

    def test_type(self):
        zero_cycle = cycle("UCU")

        self.assertEqual(str(type(zero_cycle)), '<class \'generator\'>')

    def test_step(self):
        first_cycle = cycle("TEST")

        self.assertEqual(next(first_cycle), 'T')
        self.assertEqual(next(first_cycle), 'E')
        self.assertEqual(next(first_cycle), 'S')
        self.assertEqual(next(first_cycle), 'T')

    def test_repeat(self):
        second_cycle = cycle("T")

        self.assertEqual(next(second_cycle), 'T')
        self.assertEqual(next(second_cycle), 'T')
        self.assertEqual(next(second_cycle), 'T')


class TestCombinations(unittest.TestCase):

    def test_type(self):
        self.assertEqual(str(type(combinations(0, 3))),
                         '<class \'generator\'>')

    def test_zero(self):
        self.assertEqual(list(combinations(0, 4)), [()])
        self.assertEqual(list(combinations(0, 7)), [()])

    def test_invalid(self):
        self.assertEqual(list(combinations(10, 4)), [])
        self.assertEqual(list(combinations(8, 7)), [])
        self.assertEqual(list(combinations(2, 1)), [])

    def test_regular(self):
        self.assertEqual(list(combinations(2, 3)), [(0, 1), (0, 2), (1, 2)])
        self.assertEqual(list(combinations(1, 2)), [(0,), (1,)])
        self.assertEqual(list(combinations(1, 1)), [(0,)])


class TestCombinationsReplacement(unittest.TestCase):

    def test_type(self):
        self.assertEqual(
            str(type(combinations_with_replacement(0, 3))), '<class \'generator\'>')

    def test_zero(self):
        self.assertEqual(list(combinations_with_replacement(0, 10)), [()])
        self.assertEqual(list(combinations_with_replacement(0, 3)), [()])

    def test_invalid(self):
        self.assertEqual(list(combinations_with_replacement(14, 7)), [])
        self.assertEqual(list(combinations_with_replacement(4, 3)), [])
        self.assertEqual(list(combinations_with_replacement(5, 1)), [])

    def test_regular(self):
        self.assertEqual(list(combinations_with_replacement(2, 3)), [
                         (0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)])
        self.assertEqual(
            list(combinations_with_replacement(1, 2)), [(0,), (1,)])
        self.assertEqual(list(combinations_with_replacement(1, 1)), [(0,)])


class TestRepeat(unittest.TestCase):

    def test_type(self):
        self.assertEqual(str(type(repeat(15))), '<class \'generator\'>')

    def test_string(self):
        zero_repeat = repeat('Hello')
        second_repeat = repeat('Boy')

        self.assertEqual(next(zero_repeat), 'Hello')
        self.assertEqual(next(zero_repeat), 'Hello')

        self.assertEqual(next(second_repeat), 'Boy')
        self.assertEqual(next(second_repeat), 'Boy')

    def test_list(self):
        zero_repeat = repeat([1, 2])
        second_repeat = repeat([1, 2, 3])

        self.assertEqual(next(zero_repeat), [1, 2])
        self.assertEqual(next(zero_repeat), [1, 2])

        self.assertEqual(next(second_repeat), [1, 2, 3])
        self.assertEqual(next(second_repeat), [1, 2, 3])

    def test_int(self):
        zero_repeat = repeat(1)
        second_repeat = repeat(10)

        self.assertEqual(next(zero_repeat), 1)
        self.assertEqual(next(zero_repeat), 1)

        self.assertEqual(next(second_repeat), 10)
        self.assertEqual(next(second_repeat), 10)


class TestProduct(unittest.TestCase):

    def test_type(self):
        self.assertEqual(
            str(type(product([1, 2], [4, 6]))), '<class \'generator\'>')

    def test_valid(self):
        self.assertEqual(list(product(('1', 1), [2, '2'])), [
                         ('1', 2), ('1', '2'), (1, 2), (1, '2')])
        self.assertEqual(list(product([1, 2], [4, 5])), [
                         (1, 4), (1, 5), (2, 4), (2, 5)])
        self.assertEqual(list(product('cu', [0, 5])), [
                         ('c', 0), ('c', 5), ('u', 0), ('u', 5)])


class TestPermutations(unittest.TestCase):

    def test_type(self):
        self.assertEqual(
            str(type(permutations([1, 3]))), '<class \'generator\'>')

    def test_valid(self):
        self.assertEqual(list(permutations([1, 3, 5], 2)), [
                         (1, 3), (1, 5), (3, 1), (3, 5), (5, 1), (5, 3)])
        self.assertEqual(list(permutations(
            [0, 5, -5])), [(0, 5, -5), (0, -5, 5), (5, 0, -5), (5, -5, 0), (-5, 0, 5), (-5, 5, 0)])


if __name__ == '__main__':
    unittest.main()
