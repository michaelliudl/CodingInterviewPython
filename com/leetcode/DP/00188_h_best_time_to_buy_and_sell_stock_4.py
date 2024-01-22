from typing import List
import heapq

class Solution:

    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k<=0:
            return 0
        dp=[[0]*(1+2*k) for _ in range(len(prices))]
        for i in range(1, 2*k+1, 2):
            dp[0][i] = -prices[0]
        for i in range(1, len(prices)):
            for j in range(1, 2*k+1):
                if j % 2 == 1:
                    dp[i][j]=max(dp[i-1][j], dp[i-1][j-1] - prices[i])
                else:
                    dp[i][j]=max(dp[i-1][j], dp[i-1][j-1] + prices[i])
        return dp[len(prices)-1][2*k]

import unittest

class TestSolution(unittest.TestCase):
    def testMaxProfit(self):
        s = Solution()
        self.assertEqual(s.maxProfit(k = 2, prices = [2,4,1]), 2)
        self.assertEqual(s.maxProfit(k = 2, prices = [3,2,6,5,0,3]), 7)
        


if __name__ == '__main__':
    unittest.main()