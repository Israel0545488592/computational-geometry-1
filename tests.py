import unittest
from utils import *

class Test(unittest.TestCase):

    def test_orient(self):

        self.assertTrue(orient((0, 0), (0, 1), (-1, 1)) > 0)
        self.assertTrue(orient((0, 0), (0, 1), (0, 2)) == 0)
        self.assertTrue(orient((0, 0), (0, 1), (1, 1)) < 0)

    def test_find_tangent_point(self):

        self.assertEqual(find_tangent_point( * read_convex_orign('input/input1.txt')), 1)
        self.assertEqual(find_tangent_point( * read_convex_orign('input/input2.txt')), 153)
        self.assertEqual(find_tangent_point( * read_convex_orign('input/input3.txt')), 32)

        

if __name__ == '__main__': unittest.main()