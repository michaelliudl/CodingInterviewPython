from typing import List

class Solution:

    # dp[i][0] is cash while holding stock on day i
    # dp[i][1] is cash while NOT holdin stock on day i
    # dp[i][0]=max(dp[i-1][0], dp[i-1][1]-prices[i])
    # dp[i][1]=max(dp[i-1][1], dp[i-1][0]+prices[i])
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp=[[0]*2 for _ in range(len(prices))]
        dp[0][0]=-prices[0]
        dp[0][1]=0
        for i in range(1,len(prices)):
            dp[i][0]=max(dp[i-1][0], dp[i-1][1]-prices[i])
            dp[i][1]=max(dp[i-1][1], dp[i-1][0]+prices[i])
        return dp[len(prices)-1][1]

    # Total profit is sum of all positive profit from ajacent days
    def maxProfitGreedy(self, prices: List[int]) -> int:
        if not prices:
            return 0
        total=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                total+=prices[i]-prices[i-1]
        return total
        

import unittest

class TestSolution(unittest.TestCase):
    def testMaxProfit(self):
        s = Solution()
        self.assertEqual(s.maxProfit(prices = [7,1,5,3,6,4]), 7)
        


if __name__ == '__main__':
    unittest.main()