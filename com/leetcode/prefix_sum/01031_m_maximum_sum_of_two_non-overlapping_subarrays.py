from typing import List

class Solution:

    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        if not nums:
            return 0
        prefixSum = [0] * (len(nums) + 1)
        for i in range(1, len(prefixSum)):
            prefixSum[i] = prefixSum[i-1] + nums[i-1]
        longLen, shortLen = max(firstLen, secondLen), min(firstLen, secondLen)
        ans = 0
        for i in range(longLen, len(prefixSum)):
            longSum = prefixSum[i] - prefixSum[i - longLen]
            for j in range(shortLen, i - longLen + 1):
                shortSum = prefixSum[j] - prefixSum[j - shortLen]
                ans = max(ans, longSum + shortSum)
            for j in range(i + shortLen, len(prefixSum)):
                shortSum = prefixSum[j] - prefixSum[j - shortLen]
                ans = max(ans, longSum + shortSum)
        return ans

import unittest

class TestSolution(unittest.TestCase):
    def testMaxSumTwoNoOverlap(self):
        s = Solution()
        self.assertEqual(s.maxSumTwoNoOverlap(nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2), 20)
        self.assertEqual(s.maxSumTwoNoOverlap(nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2), 29)
        self.assertEqual(s.maxSumTwoNoOverlap(nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen = 3), 31)
        


if __name__ == '__main__':
    unittest.main()