from typing import List

class Solution:

    # dp[i] is number of ways to decode substring ends at i-1
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0': return 0
        n=len(s)
        dp=[0]*(n+1)
        dp[0],dp[1]=1,1
        for i in range(2,n+1):
            if s[i-1] == '0':
                dp[i] = dp[i-2] if s[i-2] in {'1','2'} else 0          # Match 10,20
            elif s[i-1] in {'7','8','9'}:
                dp[i] = dp[i-1]
                dp[i] += dp[i-2] if s[i-2] == '1' else 0     # Match 17-19
            else:
                dp[i] = dp[i-1]                      # Match 1-6
                dp[i] += dp[i-2] if s[i-2] in {'1', '2'} else 0      # Match 11-16, 21-26
        return dp[n]


import unittest

class TestSolution(unittest.TestCase):
    def testNumDecodings(self):
        s = Solution()
        self.assertEqual(s.numDecodings(s = '226'), 3)
        self.assertEqual(s.numDecodings(s = '06'), 0)
        self.assertEqual(s.numDecodings(s = '10'), 1)
        self.assertEqual(s.numDecodings(s = '12'), 2)
        


if __name__ == '__main__':
    unittest.main()