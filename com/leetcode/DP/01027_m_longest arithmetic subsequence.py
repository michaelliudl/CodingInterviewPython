from typing import List

class Solution:

    def longestArithSeqLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        result = 0
        dp = [[0] * 1001 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j] + 500
                dp[i][diff] = max(2, dp[j][diff] + 1)
                result = max(result, dp[i][diff])
        return result


import unittest

class TestSolution(unittest.TestCase):
    def testLongestArithSeqLength(self):
        s = Solution()
        self.assertEqual(s.longestArithSeqLength(nums = [12,28,13,6,34,36,53,24,29,2,23,0,22,25,53,34,23,50,35,43,53,11,48,56,44,53,31,6,31,57,46,6,17,42,48,28,5,24,0,14,43,12,21,6,30,37,16,56,19,45,51,10,22,38,39,23,8,29,60,18]), 4)
        self.assertEqual(s.longestArithSeqLength(nums = [83,20,17,43,52,78,68,45]), 2)
        self.assertEqual(s.longestArithSeqLength(nums = [3,6,9,12]), 4)
        self.assertEqual(s.longestArithSeqLength(nums = [9,4,7,2,10]), 3)
        self.assertEqual(s.longestArithSeqLength(nums = [20,1,15,3,10,5,8]), 4)


if __name__ == '__main__':
    unittest.main()