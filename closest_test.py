import unittest
from closest import closest


class ClosestTest(unittest.TestCase):
    def test_1_single(self):
        self.assertEqual(closest([1], 1, 1), [1])

    def test_2_simple(self):
        self.assertEqual(closest([1, 2, 3, 4, 5], 3, 3), [2, 3, 4])

    def test_3_left(self):
        self.assertEqual(closest([1, 2, 3, 4, 5], 1, 3), [1, 2, 3])

    def test_4_right(self):
        self.assertEqual(closest([1, 2, 3, 4, 5], 5, 3), [3, 4, 5])

    def test_5_all_center(self):
        self.assertEqual(closest([1, 2, 3, 4, 5], 3, 5), [1, 2, 3, 4, 5])

    def test_6_all(self):
        self.assertEqual(closest([1, 2, 3, 4, 5], 2, 5), [1, 2, 3, 4, 5])

    def test_7_nonexisting_center(self):
        self.assertEqual(closest([1, 2, 4, 5], 3, 2), [2, 4])

    def test_8_nonexisting_left(self):
        self.assertEqual(closest([1, 2, 3, 4, 5], -1, 2), [1, 2])

    def test_7_nonexisting_right(self):
        self.assertEqual(closest([1, 2, 3, 4, 5], 10, 2), [4, 5])

    def test_larger(self):
        self.assertEqual(
            closest([4, 5, 28, 34, 47, 57, 61, 81, 85, 93], 61, 3), [47, 57, 81]
        )
