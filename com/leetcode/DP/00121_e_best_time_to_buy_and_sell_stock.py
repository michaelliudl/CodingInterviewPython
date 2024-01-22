from typing import List

class Solution:

    # dp[i][0] is cash on hand if holding stock on day i. It starts with 0 and is negative after buying.
    # dp[i][1] is cash on hand if NOT holding stock on day i.
    # Because only buy and sell once
    # dp[i][0] = max(-prices[i], dp[i-1][0])        Either buy on day i or hold from buying day i-1 or earlier
    # dp[i][1] = max(0, prices[i] + dp[i-1][0])     Either never bought or sell on day i from holding from day i-1 or earlier
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp=[[0]*2 for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1,len(prices)):
            dp[i][0] = max(-prices[i], dp[i-1][0])
            dp[i][1] = max(dp[i-1][1], prices[i] + dp[i-1][0])
        return dp[len(prices)-1][1]
    
    def maxProfitRolling(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp=[[0]*2 for _ in range(2)]
        dp[0][0]=-prices[0]
        dp[0][1]=0
        for i in range(1,len(prices)):
            dp[i%2][0]=max(-prices[i], dp[(i-1)%2][0])
            dp[i%2][1]=max(dp[(i-1)%2][1], prices[i]+dp[((i-1)%2)][0])
        return dp[(len(prices)-1)%2][1]


    def maxProfitGreedy(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minPrice=float('inf')
        r=0
        for p in prices:
            minPrice=min(minPrice,p)
            r=max(r, (p-minPrice))
        return r


import unittest

class TestSolution(unittest.TestCase):
    def testSubsets(self):
        s = Solution()
        self.assertEqual(s.subsets(nums = [1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        self.assertEqual(s.subsets(nums = [0]), [[],[0]])
        


if __name__ == '__main__':
    unittest.main()