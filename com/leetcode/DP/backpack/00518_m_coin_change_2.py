from typing import List

class Solution:

    # Brute force loop and backtrack recursion

    # dp[j] is number of combinations that forms j
    # dp[j] += dp[j-coin(i)]
    def change(self, amount: int, coins: List[int]) -> int:
        if not coins or amount<0:
            return 0
        dp=[0]*(amount+1)
        dp[0]=1
        for coin in coins:                      # For combinations, iterate items first then backpack size
            for j in range(coin, amount+1):
                dp[j]+=dp[j-coin]
        return dp[amount]

        

import unittest

class TestSolution(unittest.TestCase):
    def testChange(self):
        s = Solution()
        self.assertEqual(s.change(amount = 5, coins = [1,2,5]), 4)
        self.assertEqual(s.change(amount = 3, coins = [2]), 0)
        self.assertEqual(s.change(amount = 10, coins = [10]), 1)
        self.assertEqual(s.change(amount = 0, coins = [7]), 1)


if __name__ == '__main__':
    unittest.main()