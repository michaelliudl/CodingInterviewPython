from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # Binary search within [max(nums), sum(nums)]
    # For each middle value, greedily finding subarrays whose sum is less than mid, and total such subarrays equal to k
    def splitArray(self, nums: List[int], k: int) -> int:

        def canSplit(minSum):
            splits,subSum = 1,0
            for num in nums:
                subSum += num
                if subSum > minSum:
                    splits += 1
                    subSum = num
            return splits <= k
            

        if not nums: return 0
        low,high = max(nums), sum(nums)
        while low < high:
            mid = low + (high - low) // 2
            if canSplit(mid):
                high = mid
            else:
                low = mid + 1
        return low

import unittest

class TestSolution(unittest.TestCase):
    def testSplitArray(self):
        s = Solution()
        self.assertEqual(s.splitArray(nums = [1,4,4], k = 3), 4)
        self.assertEqual(s.splitArray(nums = [7,2,5,10,8], k = 2), 18)
        self.assertEqual(s.splitArray(nums = [1,2,3,4,5], k = 2), 9)


if __name__ == '__main__':
    unittest.main()