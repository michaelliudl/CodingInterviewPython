from typing import List

class Solution:

    # dp[i] is number of ways at length i
    # dp[i] = 2 * dp[i-1] + dp[i-3]
    def numTilings(self, n: int) -> int:
        if n < 2: return n
        dp = [0] * (n+1)
        dp[0], dp[1], dp[2] = 1, 1, 2
        for i in range(3, n+1):
            dp[i] = (2 * dp[i-1] + dp[i-3]) % (10**9 + 7)
        return dp[n]
    
import unittest

class TestSolution(unittest.TestCase):
    def testNumTilings(self):
        s = Solution()
        self.assertEqual(s.numTilings(n=3), 5)
        self.assertEqual(s.numTilings(n=10), 1255)
        


if __name__ == '__main__':
    unittest.main()