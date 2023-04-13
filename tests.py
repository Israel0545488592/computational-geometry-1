import unittest
from convex_tangent import *

class Test(unittest.TestCase):

    def test_orient(self):

        self.assertTrue(orient((0, 0), (0, 1), (-1, 1)) > 0)
        self.assertTrue(orient((0, 0), (0, 1), (0, 2)) == 0)
        self.assertTrue(orient((0, 0), (0, 1), (1, 1)) < 0)

    def test_find_tangent_point(self):

        self.find_tangent_point()

if __name__ == '__main__':

    unittest.main()