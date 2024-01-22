from typing import List

class Solution:

    # No crossing means numbers appear in same order
    # Same as LCS
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        if not nums1 or not nums2:
            return 0
        m,n,longest=len(nums1),len(nums2),0
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j], dp[i][j-1])
                longest=max(longest, dp[i][j])
        return longest

import unittest

class TestSolution(unittest.TestCase):
    def testIntegerBreak(self):
        s = Solution()
        self.assertEqual(s.integerBreak(n=10), 36)
        


if __name__ == '__main__':
    unittest.main()