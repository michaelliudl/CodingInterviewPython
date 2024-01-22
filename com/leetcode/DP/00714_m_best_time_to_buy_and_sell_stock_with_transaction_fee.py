from typing import List

class Solution:

    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        n=len(prices)
        dp=[[0]*2 for _ in range(n)]
        dp[0][0] = -prices[0]
        for i in range(1,n):
            dp[i][0]=max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1]=max(dp[i-1][1], dp[i-1][0] + prices[i] - fee)
        return dp[n-1][1]

import unittest

class TestSolution(unittest.TestCase):
    def testMaxProfit(self):
        s = Solution()
        self.assertEqual(s.maxProfit(prices = [1,3,2,8,4,9], fee = 2), 8)
        self.assertEqual(s.maxProfit(prices = [1,3,7,5,10,3], fee = 3), 6)
        


if __name__ == '__main__':
    unittest.main()