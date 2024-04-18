from typing import List

class Solution:

    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        if not nums or len(nums) < k * 3:
            return []
        n = len(nums) - k + 1
        kSubSums = [0] * n          # kSubSums[i] = sum(nums[i:i+k])
        curSum = 0
        for i, num in enumerate(nums):
            curSum += num
            if i >= k:
                curSum -= nums[i - k]
            if i >= k - 1:
                kSubSums[i - (k - 1)] = curSum
        
        leftIndex = [0] * n         # leftIndex[i] is index in [0..i] which has max value in kSubSums[0..i]
        maxIndex = 0
        for i in range(n):
            if kSubSums[i] > kSubSums[maxIndex]:
                maxIndex = i
            leftIndex[i] = maxIndex
        
        rightIndex = [0] * n        # rightIndex[i] is index in [i..n-1] which has max value in kSubSums[i..n-1]
        maxIndex = n - 1
        for i in range(n - 1, -1, -1):
            if kSubSums[i] >= kSubSums[maxIndex]:
                maxIndex = i
            rightIndex[i] = maxIndex
        
        result = []
        maxSubSum = 0
        for i in range(k, n - k):
            subSum = kSubSums[leftIndex[i - k]] + kSubSums[i] + kSubSums[rightIndex[i + k]]
            if subSum > maxSubSum:
                maxSubSum = subSum
                result = [leftIndex[i - k], i, rightIndex[i + k]]
        return result


import unittest

class TestSolution(unittest.TestCase):
    def testMaxSumOfThreeSubarrays(self):
        s = Solution()
        self.assertEqual(s.maxSumOfThreeSubarrays(nums = [1,2,1,2,6,7,5,1], k = 2), [0,3,5])
        self.assertEqual(s.maxSumOfThreeSubarrays(nums = [1,2,1,2,1,2,1,2,1], k = 2), [0,2,4])

if __name__ == '__main__':
    unittest.main()