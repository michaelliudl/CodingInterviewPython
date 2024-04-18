from typing import List
import itertools

class Solution:

    # Similar to 907 and 84.
    # 1 pass to get product of min value and subarray sub
    def maxSumMinProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # Same as 84, add [0] at first and last
        nums = [0] + nums + [0]
        n = len(nums)
        prefixSum = [0] * (n + 1)
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]
        
        stack = []
        res = 0
        for i in range(n):
            while stack and nums[i] < nums[stack[-1]]:
                minVal = nums[stack.pop()]
                subSum = prefixSum[i] - prefixSum[stack[-1] + 1]
                res = max(res, minVal * subSum)
            stack.append(i)
        return res % (10 ** 9 + 7)

    # Similar to 907
    # 3 passes to get `prevSmaller`, `nextSmaller`, prefix sum
    # nums[i] is min value of subarray starting at prevSmaller[i], ending at nextSmaller[i].
    # Sum of each subarray can be calculated from prefix sum.
    def maxSumMinProduct1(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        stack = []
        prevSmaller = [-1] * n
        for i in range(n):
            while stack and nums[i] < nums[stack[-1]]:
                stack.pop()
            if stack:
                prevSmaller[i] = stack[-1]
            stack.append(i)
        
        stack = []
        nextSmaller = [n] * n
        for i in range(n - 1, -1, -1):
            while stack and nums[i] <= nums[stack[-1]]:
                stack.pop()
            if stack:
                nextSmaller[i] = stack[-1]
            stack.append(i)
        
        prefixSum = [0] * (n + 1)
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]

        res = 0
        for i in range(n):
            prod = nums[i] * (prefixSum[nextSmaller[i]] - prefixSum[prevSmaller[i] + 1])
            res = max(res, prod)
        return res % (10 ** 9 + 7)


import unittest

class TestSolution(unittest.TestCase):
    def testMaxSumMinProduct(self):
        s = Solution()
        self.assertEqual(s.maxSumMinProduct(nums = [5,10,6,10,4,2,1,4,5,2,4,2,7,5,8,6,3,6,6,4]), 156)
        self.assertEqual(s.maxSumMinProduct(nums = [1,2,3,2]), 14)
        self.assertEqual(s.maxSumMinProduct(nums = [2,3,3,1,2]), 18)
        self.assertEqual(s.maxSumMinProduct(nums = [3,1,5,6,4,2]), 60)
        


if __name__ == '__main__':
    unittest.main()