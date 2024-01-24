from typing import List

class Solution:

    # Backpack volume is sum(nums)//2. Each number is weight and value.
    # DP array should be initialized to backpack size and 0 (-inf if negative value possible)
    # dp[j] = max(dp[j], dp[j-num(i)] + nums(i))    Since num is both weight and value, from dp[j]=max(dp[j], dp[j-weight(i)] + value(i))
    # 1D DP, loop items forwards first, then backpack backwards from volume to each item's weight(included)
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return False
        s=sum(nums)
        if s%2==1: return False
        n,volume=len(nums),s//2
        dp=[0]*(volume+1)
        for i in range(n):
            weight,value=nums[i],nums[i]
            for j in range(volume, weight-1, -1):
                dp[j]=max(dp[j], dp[j - weight] + value)
        return volume == dp[volume]
        

import unittest

class TestSolution(unittest.TestCase):
    def testCanPartition(self):
        s = Solution()
        self.assertEqual(s.canPartition(nums = [1,5,11,5]), True)
        self.assertEqual(s.canPartition(nums = [1,2,3,5]), False)


if __name__ == '__main__':
    unittest.main()