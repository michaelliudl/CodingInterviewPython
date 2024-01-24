from typing import List
import heapq

class Solution:

    # Equivalent to the array into 2 with equal sum as much as possible
    # dp[j] = max(dp[j], dp[j - weight(i)] + value(i))    
    def lastStoneWeightII(self, stones: List[int]) -> int:
        if not stones:
            return 0
        if len(stones)<2:
            return stones[0]
        n,total=len(stones),sum(stones)
        volume=total//2                      # Take floor as volume which will be <= total/2 
        dp=[0]*(volume+1)
        for i in range(n):
            weight,value=stones[i],stones[i]
            for j in range(volume, weight-1, -1):
                dp[j]=max(dp[j], dp[j - weight] + value)
        return total - dp[volume]*2



import unittest

class TestSolution(unittest.TestCase):
    def testLastStoneWeightII(self):
        s = Solution()
        self.assertEqual(s.lastStoneWeightII(stones = [2,7,4,1,8,1]), 1)
        self.assertEqual(s.lastStoneWeightII(stones=[31,26,33,21,40]), 5)



if __name__ == '__main__':
    unittest.main()