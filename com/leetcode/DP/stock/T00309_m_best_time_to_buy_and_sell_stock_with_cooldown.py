from typing import List

class Solution:

    # Define 4 possible states for each day i
    #       0 - buy or holding stock today
    #       1 - not holding today
    #       2 - sold today
    #       3 - cooldown today
    # dp[i][j] is cash on hand for day i while in each possible state
    # dp[i][0] = max(dp[i-1][0],    dp[i-1][1] - prices[i],     dp[i-1][3] - prices[i])
    #               Hold prev       Not hold prev, buy today    Cooldown yday, buy today
    # dp[i][1] = max(dp[i-1][1],    dp[i-1][3])
    #               Not hold prev   Cooldown yday
    # dp[i][2] = dp[i-1][0] + prices[i]     # Must be state 0 yday
    # dp[i][3] = dp[i-1][2]                 # Must sold yday and be cooldown today
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n=len(prices)
        dp=[[0]*4 for _ in range(n)]
        dp[0][0] = -prices[0]
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i], dp[i-1][3] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][3])
            dp[i][2] = dp[i-1][0] + prices[i]
            dp[i][3] = dp[i-1][2]
        return max(dp[n-1][1], dp[n-1][2], dp[n-1][3])  # Must not have stock last day. Max profit can be from state 1, 2 or 3

        

import unittest

class TestSolution(unittest.TestCase):
    def testMaxProfit(self):
        s = Solution()
        self.assertEqual(s.maxProfit(prices = [1,2,3,0,2]), 3)
        self.assertEqual(s.maxProfit(prices = [1]), 0)
        


if __name__ == '__main__':
    unittest.main()