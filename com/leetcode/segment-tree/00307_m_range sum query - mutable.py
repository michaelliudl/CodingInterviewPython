from typing import List

# Segment tree / Fenwick tree TODO
class NumArray1:

    def __init__(self, nums: List[int]):
        pass

    def update(self, index: int, val: int) -> None:
        pass

    def sumRange(self, left: int, right: int) -> int:
        pass

# Prefix sum time out.
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        n = len(nums)
        self.prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            self.prefix[i] = self.prefix[i - 1] + self.nums[i - 1]

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        n = len(self.nums)
        for i in range(index + 1, n + 1):
            self.prefix[i] += diff

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

class Solution:
    pass

import unittest

class TestSolution(unittest.TestCase):
    def testNumArray(self):
        na = NumArray([1, 3, 5])
        self.assertEqual(na.sumRange(0, 2), 9)
        na.update(1, 2)
        self.assertEqual(na.sumRange(0, 2), 8)
        


if __name__ == '__main__':
    unittest.main()