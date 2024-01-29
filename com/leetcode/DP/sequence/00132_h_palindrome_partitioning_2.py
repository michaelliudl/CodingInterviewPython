from typing import List

class Solution:

    # palin[i][j]   Set to if substring s between i and j (inclusive) is palindrome

    # dp[i]     Set to min number to make cuts all palindrome for substring of s between 0 and i
    # dp[i] = min(dp[i], dp[j]+1)   if substring s between j+1 and i is palindrome. Loop possible cuts j between 0 and i-1. 
    def minCut(self, s: str) -> int:
        if not s: return 0
        n=len(s)

        palin=[[False]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if i==j:
                    palin[i][j]=True
                elif s[i]==s[j]:
                    if j-i==1:
                        palin[i][j]=True
                    else:
                        palin[i][j]=palin[i+1][j-1]
        
        dp=[i for i in range(n)]    # Initialize min cut array to max possible cuts
        for i in range(1,n):
            if palin[0][i]:
                dp[i]=0
            else:
                for j in range(i):
                    if palin[j+1][i]:
                        dp[i] = min(dp[i], dp[j]+1)
        return dp[n-1]


import unittest

class TestSolution(unittest.TestCase):
    def testMinCut(self):
        s = Solution()
        self.assertEqual(s.minCut(s = "aab"), 1)
        self.assertEqual(s.minCut(s = "a"), 0)
        self.assertEqual(s.minCut(s = "ab"), 1)
        self.assertEqual(s.minCut(s = "aabc"), 2)
        


if __name__ == '__main__':
    unittest.main()