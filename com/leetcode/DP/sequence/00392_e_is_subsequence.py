from typing import List

class Solution:

    # dp[i][j] is length of LCS (contains all characters in s) between substring ending at i-1 in s (s[:i]) and ending at j-1 in t (t[:j])
    # dp[i][j] = (dp[i-1][j-1] + 1) if s[i-1]==t[j-1] else: dp[i][j-1] (only backtrack j since all characters in s must be considered)
    def isSubsequence(self, s: str, t: str) -> bool:
        m,n=len(s),len(t)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=dp[i][j-1]     # Only move back j since all characters in s must be considered
        return dp[m][n]==m

    # Two pointer
    def isSubsequenceTwoPointer(self, s: str, t: str) -> bool:
        i,last=0,0
        while i<len(s):
            found=False
            for j in range(last,len(t)):
                if t[j]==s[i]:
                    found=True
                    last=j+1
                    break
            if found:
                i+=1
            else:
                break
        return i==len(s)
            


import unittest

class TestSolution(unittest.TestCase):
    def testIsSubsequence(self):
        s = Solution()
        self.assertEqual(s.isSubsequence(s = "abc", t = "ahbgdc"), True)
        self.assertEqual(s.isSubsequence(s = "axc", t = "ahbgdc"), False)
        


if __name__ == '__main__':
    unittest.main()