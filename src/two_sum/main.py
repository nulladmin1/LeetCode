from typing import List, Tuple


class Solution:
    def two_sum(self, nums: List[int], target: int) -> Tuple[int, int]:
        hm = {}
        for i, n in enumerate(nums):
            hm[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hm and hm[diff] != i:
                return i, hm[diff]

def main():
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print("Nums: ", nums)
    print("Target: ", target)
    print(solution.two_sum(nums, target))