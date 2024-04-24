from typing import List
import math

class Solution:
    # Followup of 2865
    # Use monotonic increasing stack to calculate max possible sum for each index, both forwards and backwards
    # Find max of (forwards[i] + backwards[i] - maxHeights[i]) since maxHeights[i] is included in both forwards and backwards
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        if not maxHeights:
            return 0
        nums = maxHeights
        n = len(nums)

        forwards = [0] * n
        stack = []
        curSum = 0              # Accumulate max sum of possible increasing numbers forwards
        for i in range(n):
            while stack and nums[i] < nums[stack[-1]]:
                prevMaxIndex = stack.pop()
                prevMax = nums[prevMaxIndex]
                prevSum = prevMax * (prevMaxIndex - (stack[-1] if stack else -1))
                curSum -= prevSum       # Since current is lower, need to remove all sums from previous higher ones
            curSum += nums[i] * (i - (stack[-1] if stack else -1))  # Add back all sums with current as highest
            forwards[i] = curSum
            stack.append(i)

        backwards = [0] * n
        stack = []
        curSum = 0
        for i in range(n - 1, -1, -1):
            while stack and nums[i] < nums[stack[-1]]:
                prevMaxIndex = stack.pop()
                prevMax = nums[prevMaxIndex]
                prevSum = prevMax * ((stack[-1] if stack else n) - prevMaxIndex)
                curSum -= prevSum
            curSum += nums[i] * ((stack[-1] if stack else n) - i)
            backwards[i] = curSum
            stack.append(i)

        res = 0
        for i in range(n):
            res = max(res, forwards[i] + backwards[i] - nums[i])
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testMaximumSumOfHeights(self):
        s = Solution()
        self.assertEqual(s.maximumSumOfHeights(maxHeights = [5,3,4,1,1]), 13)
        self.assertEqual(s.maximumSumOfHeights(maxHeights = [6,5,3,9,2,7]), 22)
        self.assertEqual(s.maximumSumOfHeights(maxHeights = [3,2,5,5,2,3]), 18)


if __name__ == '__main__':
    unittest.main()