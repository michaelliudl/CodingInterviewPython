from typing import List
import heapq

class Solution:

    # Split into two group of numbers left and right that makes left+right=total and left-right=target
    # Find how many combinations to get left (or right) where left=(total+target)//2 is volume
    # dp[j] means number of ways to fill backpack volume of j
    # dp[j] += dp[j-nums(i)]    Sum all the ways to fill volume j with each nums(i)
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if not nums: return 0
        total,n=sum(nums),len(nums)
        if abs(target)>total: return 0
        if (target+total)%2==1: return 0        # Only have solution if both are odd or both even
        volume=(target+total)//2
        dp=[0]*(volume+1)
        dp[0]=1                                 # Must initialize as 1 to sum
        for i in range(n):
            weight=nums[i]
            for j in range(volume, weight-1, -1):
                dp[j]+=dp[j-weight]
        return dp[volume]




import unittest

class TestSolution(unittest.TestCase):
    def testFindTargetSumWays(self):
        s = Solution()
        self.assertEqual(s.findTargetSumWays(nums = [1,1,1,1,1], target = 3), 5)
        self.assertEqual(s.findTargetSumWays(nums = [1], target = 1), 1)
        self.assertEqual(s.findTargetSumWays(nums = [100], target = -200), 0)



if __name__ == '__main__':
    unittest.main()