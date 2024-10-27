from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_sum = []
        current_sum = 0
        for num in nums:
            current_sum += num
            self.prefix_sum.append(current_sum)
    def sumRange(self, left: int, right: int) -> int:
        r = self.prefix_sum[right]
        l = self.prefix_sum[left - 1] if left > 0 else 0
        n = r - l
        return n

    # Your NumArray object will be instantiated and called as such:
    # obj = NumArray(nums)
    # param_1 = obj.sumRange(left,right)

def main():
    nums = [-2, 0, 3, -5, 2, -1]
    num_array = NumArray(nums)
    print(num_array.prefix_sum)
    print(num_array.sumRange(2, 5))

if __name__ == '__main__':
    main()