from typing import List

class Solution:

    # dp[i][j] is longest subarray length for subarray ended at (i-1) in first and subarray ended at (j-1) in second
    # dp[i][j] = dp[i-1][j-1] + 1 if nums1[i-1]==nums2[j-1]
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if not nums1 or not nums2:
            return 0
        m,n,longest=len(nums1),len(nums2),0
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                    longest=max(longest,dp[i][j])
        return longest
        
    def findLengthOneDArray(self, nums1: List[int], nums2: List[int]) -> int:
        if not nums1 or not nums2:
            return 0
        m,n,longest=len(nums1),len(nums2),0
        dp=[0]*(n+1)                    # dp array with second input length
        for i in range(1,m+1):          # Scan input 1 first
            for j in range(n, 0, -1):   # Backward scan of input 2
                if nums1[i-1]==nums2[j-1]:
                    dp[j]=dp[j-1]+1
                else:
                    dp[j]=0             # This is required
                longest=max(longest, dp[j])
        return longest



import unittest

class TestSolution(unittest.TestCase):
    def testSubsets(self):
        s = Solution()
        self.assertEqual(s.subsets(nums = [1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        self.assertEqual(s.subsets(nums = [0]), [[],[0]])
        


if __name__ == '__main__':
    unittest.main()