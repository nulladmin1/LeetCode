import unittest
from merge_strings_alternatively import Solution

class TestTwoSum(unittest.TestCase):
    solution = Solution()
    def test_normal(self):
        word1 = "abc"
        word2 = "pqr"
        expected_solution = "apbqcr"
        self.assertEqual(self.solution.merge_alternately(word1, word2), expected_solution)
    def test_extra_characters(self):
        word1 = "abc"
        word2 = "pqrst"
        expected_solution = "apbqcrst"
        self.assertEqual(self.solution.merge_alternately(word1, word2), expected_solution)

if __name__ == "__main__":
    unittest.main()
