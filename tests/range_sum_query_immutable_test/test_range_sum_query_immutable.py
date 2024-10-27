import unittest
from range_sum_query_immutable import NumArray

class TestRangeSumQueryImmutable(unittest.TestCase):
    nums = [-2, 0, 3, -5, 2, -1]
    def test_normal(self):
        nums = self.nums
        num_array = NumArray(nums)
        left = 0
        right = 2
        expected_solution = 1
        self.assertEqual(num_array.sumRange(left, right), expected_solution)
    def test_2(self):
        nums = self.nums
        num_array = NumArray(nums)
        left = 2
        right = 5
        expected_solution = -1
        self.assertEqual(num_array.sumRange(left, right), expected_solution)
    def test_3(self):
        nums = self.nums
        num_array = NumArray(nums)
        left = 0
        right = 5
        expected_solution = -3
        self.assertEqual(num_array.sumRange(left, right), expected_solution)

if __name__ == "__main__":
    unittest.main()
