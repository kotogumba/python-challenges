import unittest
from three_sum import threeSum

class TestThreeSum(unittest.TestCase):
    def test_three_sum(self):
        self.assertEqual(threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2],[ -1, 0, 1]])

    def test_three_sum_2(self):
        self.assertEqual(threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])


if __name__ == '__main__':
    unittest.main()
