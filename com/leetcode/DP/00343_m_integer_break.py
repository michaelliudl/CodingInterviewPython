from typing import List

class Solution:

    # dp[i] = max product from breaking i
    # dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
    def integerBreak(self, n: int) -> int:
        if n<=0:
            return n
        dp=[0]*(n+1)
        dp[2]=1
        for i in range(3, n+1):
            for j in range(1,i//2+1):
                dp[i]=max(dp[i], max(j*(i-j), j*dp[i-j]))
        # print(dp)
        return dp[n]

import unittest

class TestSolution(unittest.TestCase):
    def testIntegerBreak(self):
        s = Solution()
        self.assertEqual(s.integerBreak(n=10), 36)
        


if __name__ == '__main__':
    unittest.main()