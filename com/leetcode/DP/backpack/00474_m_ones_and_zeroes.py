from typing import List

class Solution:

    # Brute force loop and backtrack recursion

    # dp[j] is min number of coins to make amount j
    # dp[j] = min(dp[j], dp[j-weight(i)] + 1)   Each coin is weight, value is 1
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or amount<=0:
            return 0
        coins.sort()
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        for coin in coins:
            for j in range(coin, amount+1):
                dp[j]=min(dp[j], dp[j-coin] + 1)
        return -1 if dp[amount]==float('inf') else dp[amount]


        

import unittest

class TestSolution(unittest.TestCase):
    def testCoinChange(self):
        s = Solution()
        self.assertEqual(s.coinChange(coins = [1,2,5], amount = 11), 3)
        self.assertEqual(s.coinChange(coins = [2], amount = 3), -1)
        self.assertEqual(s.coinChange(coins = [1], amount = 0), 0)


if __name__ == '__main__':
    unittest.main()