import unittest
from two_sum import twoSum

class TestTwoSum(unittest.TestCase):
    def test_example_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        result = twoSum(nums, target)
        self.assertEqual(result, [0, 1])

    def test_example_2(self):
        nums = [3, 2, 4]
        target = 6
        result = twoSum(nums, target)
        self.assertEqual(result, [1, 2])

    def test_example_3(self):
        nums = [3, 3]
        target = 6
        result = twoSum(nums, target)
        self.assertEqual(result, [0, 1])

    def test_same_number(self):
        nums = [5, 5]
        target = 10
        result = twoSum(nums, target)
        self.assertEqual(result, [0, 1])

    def test_negative_numbers(self):
        nums = [-2, 7, -11, 15]
        target = 4
        result = twoSum(nums, target)
        self.assertEqual(result, [2, 3])

if __name__ == '__main__':
    unittest.main()
