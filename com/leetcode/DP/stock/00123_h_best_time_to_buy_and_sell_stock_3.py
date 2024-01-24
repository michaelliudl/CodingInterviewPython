from typing import List
import heapq

class Solution:

    # dp[i][0]  Cash on hand if doing nothing, always 0
    # dp[i][1]  Cash on hand if FIRST time owning stock on day i
    # dp[i][2]  Cash on hand if FIRST time NOT owning stock on day i
    # dp[i][3]  Cash on hand if SECOND time owning stock on day i
    # dp[i][4]  Cash on hand if SECOND time NOT owning stock on day i

    # dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
    # dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
    # dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
    # dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i])
    def maxProfitDP(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp=[[0]*5 for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0
        dp[0][3] = -prices[0]
        dp[0][4] = 0
        for i in range(1,len(prices)):
            dp[i][1]=max(dp[i-1][1], dp[i-1][0] - prices[i])
            dp[i][2]=max(dp[i-1][2], dp[i-1][1] + prices[i])
            dp[i][3]=max(dp[i-1][3], dp[i-1][2] - prices[i])
            dp[i][4]=max(dp[i-1][4], dp[i-1][3] + prices[i])
        return dp[len(prices)-1][4]
        
    # Create 2 arrays to store max profit for each day
    # Calc first array of profits forward, using min price
    # Calc second array of profits backward, using max price
    # Find max of sum of each day
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        forwardProfits, backwardProfits = [0]*len(prices), [0]*len(prices)

        minPrice=prices[0]
        for i in range(1,len(prices)):
            minPrice=min(minPrice, prices[i])
            forwardProfits[i]=max(forwardProfits[i-1], prices[i] - minPrice)

        maxPrice=prices[-1]
        for i in range(-2, -len(prices)-1, -1):
            maxPrice=max(maxPrice, prices[i])
            backwardProfits[i]=max(backwardProfits[i+1], maxPrice - prices[i])

        total=0
        for i in range(len(prices)):
            total = max(total, forwardProfits[i] + backwardProfits[i])
        return total

import unittest

class TestSolution(unittest.TestCase):
    def testMaxProfit(self):
        s = Solution()
        self.assertEqual(s.maxProfit(prices = [3,3,5,0,0,3,1,4]), 6)
        self.assertEqual(s.maxProfit(prices = [1,2,3,4,5]), 4)
        self.assertEqual(s.maxProfit(prices = [7,6,4,3,1]), 0)
        


if __name__ == '__main__':
    unittest.main()