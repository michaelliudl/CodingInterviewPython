from typing import List

class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n,r,subSum=len(nums),nums[0],nums[0]
        for i in range(1,n):
            subSum=max(subSum+nums[i], nums[i])
            r=max(r, subSum)
        return r

    # dp[i] is max sum of subarray ended at i
    # dp[i] = max(dp[i-1] + nums[i], nums[i])
    def maxSubArrayDPNArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n,r=len(nums),-float('inf')
        dp=[0]*n
        for i,v in enumerate(nums):
            dp[i]=max(dp[i-1]+nums[i], nums[i]) if i>0 else nums[i]
            r=max(r,dp[i])
        return r

    def maxSubArrayDPCArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n,r=len(nums),-float('inf')
        dp=[0]*2
        for i,v in enumerate(nums):
            dp[i%2]=max(dp[(i-1)%2]+nums[i], nums[i]) if i>0 else nums[i]
            r=max(r, dp[i%2])
        return r

    # Greedy
    def maxSubArrayGreedy(self, nums: List[int]) -> int:
        if not nums:
            return 0
        r,sumSub=-float('inf'),0
        for _,v in enumerate(nums):
            sumSub+=v
            r=max(r,sumSub)
            if sumSub<0:
                sumSub=0
        return r
    
        

    # Brute
    def maxSubArrayBrute(self, nums: List[int]) -> int:
        if not nums:
            return 0
        r=-float('inf')
        for i in range(len(nums)):
            sumSub=0
            for j in range(i, len(nums)):
                sumSub+=nums[j]
                r=max(r, sumSub)
        return r


import unittest

class TestSolution(unittest.TestCase):
    def testMaxSubArray(self):
        s = Solution()
        self.assertEqual(s.maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]), 6)
        self.assertEqual(s.maxSubArray(nums = [5,4,-1,7,8]), 23)
        


if __name__ == '__main__':
    unittest.main()