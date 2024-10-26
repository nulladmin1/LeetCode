import unittest
from two_sum.main import Solution

class TestTwoSum(unittest.TestCase):
    solution = Solution()
    # Normal
    def test_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual(self.solution.two_sum(nums, target), (0, 1))
    # Negative
    def test_2(self):
        nums = [-3, 4, 3, 90]
        target = 0
        self.assertEqual(self.solution.two_sum(nums, target), (0, 2))

if __name__ == "__main__":
    unittest.main()
