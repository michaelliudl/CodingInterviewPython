from typing import List

class Solution:

    # dp[i]=dp[i-1]+1 if nums[i]>nums[i-1] else 1
    def findLengthOfLCISDP(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp=[1]*len(nums)
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                dp[i]=dp[i-1]+1
        return max(dp)

    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        slow,fast=0,0
        r=1
        while fast<len(nums):
            if fast==slow or nums[fast]>nums[fast-1]:
                fast+=1
            else:
                r=max(r, (fast-slow))
                slow=fast
        r=max(r, (fast-slow))
        return r


import unittest

class TestSolution(unittest.TestCase):
    def testSubsets(self):
        s = Solution()
        self.assertEqual(s.subsets(nums = [1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        self.assertEqual(s.subsets(nums = [0]), [[],[0]])
        


if __name__ == '__main__':
    unittest.main()