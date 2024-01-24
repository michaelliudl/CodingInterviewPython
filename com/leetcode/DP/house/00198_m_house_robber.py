from typing import List

class Solution:

    # dp[i] is max to get if take house i or not
    # dp[i] = max(dp[i-1], dp[i-2]*value[i])
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)<=2:
            return max(nums)
        dp=[0]*len(nums)
        dp[0],dp[1]=nums[0],max(nums[:2])
        for i in range(2,len(nums)):
            dp[i]=max(dp[i-1], dp[i-2]+nums[i])
        return dp[len(nums)-1]




import unittest

class TestSolution(unittest.TestCase):
    def testSubsets(self):
        s = Solution()
        self.assertEqual(s.subsets(nums = [1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        self.assertEqual(s.subsets(nums = [0]), [[],[0]])
        


if __name__ == '__main__':
    unittest.main()