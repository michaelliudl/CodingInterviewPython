from typing import List
import math

class Solution:

    # Subarray range sum = (Subarray sum of max) - (subarray sum of min)
    # Use 907 method to get sum min and reverse comparison to get sum max
    def subArrayRanges(self, nums: List[int]) -> int:

        def sumSubarrayMaxes(nums):
            nums = [math.inf] + nums + [math.inf]
            stack = []
            res = 0
            for i in range(len(nums)):
                while stack and nums[i] > nums[stack[-1]]:
                    maxIndex = stack.pop()
                    maxVal = nums[maxIndex]
                    leftSubLen = (maxIndex - stack[-1])
                    rightSubLen = (i - maxIndex)
                    res += maxVal * leftSubLen * rightSubLen
                stack.append(i)
            return res

        def sumSubarrayMins(nums):
            nums = [-math.inf] + nums + [-math.inf]
            stack = []
            res = 0
            for i in range(len(nums)):
                while stack and nums[i] < nums[stack[-1]]:
                    minIndex = stack.pop()
                    minVal = nums[minIndex]
                    leftSubLen = (minIndex - stack[-1])
                    rightSubLen = (i - minIndex)
                    res += minVal * leftSubLen * rightSubLen
                stack.append(i)
            return res

        if not nums:
            return 0
        return sumSubarrayMaxes(nums) - sumSubarrayMins(nums)

    # O(n**2), AC since 1 <= nums.length <= 1000
    def subArrayRangesBrute(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ret = 0
        n = len(nums)
        for i in range(n):
            curMin = curMax = nums[i]
            for j in range(i + 1, n):
                curMin = min(curMin, nums[j])
                curMax = max(curMax, nums[j])
                ret += (curMax - curMin)
        return ret


import unittest

class TestSolution(unittest.TestCase):
    def testsubArrayRanges(self):
        s = Solution()
        self.assertEqual(s.subArrayRanges(nums = [1,2,3]), 4)
        self.assertEqual(s.subArrayRanges(nums = [1,3,3]), 4)
        self.assertEqual(s.subArrayRanges(nums = [4,-2,-3,4,1]), 59)
        


if __name__ == '__main__':
    unittest.main()