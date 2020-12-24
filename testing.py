from eto_ne_itertools import *
import unittest


class TestCount(unittest.TestCase):

    def test_step(self):
        counter = count(1, 5)

        self.assertEqual(next(counter), 1)
        self.assertEqual(next(counter), 6)
        self.assertEqual(next(counter), 11)

    def test_empty(self):
        counter = count()

        self.assertEqual(next(counter), 0)
        self.assertEqual(next(counter), 1)


class TestCycle(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
