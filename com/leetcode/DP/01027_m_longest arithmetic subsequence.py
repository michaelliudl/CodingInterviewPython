from typing import List

class Solution:

    def longestArithSeqLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [[0, 0] for _ in range(len(nums) + 1)]
        # dp[0] = [1, nums[0]]
        for i in range(1, len(nums) + 1):
            for j in range(i):
                if j == 0:
                    dp
                numDiff = nums[i - 1] if j == 0 else (nums[i - 1] - nums[j])
                if numDiff == dp[j][1] and dp[j][0] > dp[i][0]:
                    dp[i][0] = dp[j][0] + 1
                    dp[i][1] = numDiff
        return dp[-1][0]


import unittest

class TestSolution(unittest.TestCase):
    def testLongestArithSeqLength(self):
        s = Solution()
        self.assertEqual(s.longestArithSeqLength(nums = [3,6,9,12]), 4)
        self.assertEqual(s.longestArithSeqLength(nums = [9,4,7,2,10]), 3)
        self.assertEqual(s.longestArithSeqLength(nums = [20,1,15,3,10,5,8]), 4)


if __name__ == '__main__':
    unittest.main()