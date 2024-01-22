from typing import List

class Solution:

    # dp[i][j] is true if substring s [i,j] (both included) is palindrome
    # dp[i][j] = true if (i==j) or (s[i]==s[j] and abs(i-j)==1)
    # dp[i][j] = true if (s[i]==s[j] and dp[i-1][j+1] is true) when abs(i-j)>1
    # Traverse forwards in first dimension as i and traverse backwards in second dimension as j from i
    # This calculates results from top-left to bottom-right diagno to botton-left
    def countSubstringsDP(self, s: str) -> int:
        if not s:
            return 0
        n=len(s)
        dp=[[0]*n for i in range(n)]
        for i in range(n):              # i top down
            for j in range(i,-1,-1):    # j right left from diagno
                if s[i]==s[j]:
                    if i-j<=1:          # i always >= j
                        dp[i][j]=1
                    else:
                        dp[i][j]=dp[i-1][j+1]
        return sum([sum(d) for d in dp])

    # Two pointers to expand from single and same double outwards
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        r,n=0,len(s)
        for i in range(n):
            a,b=i,i
            while a>=0 and b<n:
                if s[a]==s[b]:
                    r+=1
                    a-=1
                    b+=1
                else:
                    break
            if i+1<n and s[i]==s[i+1]:
                a,b=i,i+1
                while a>=0 and b<n:
                    if s[a]==s[b]:
                        r+=1
                        a-=1
                        b+=1
                    else:
                        break
        return r


import unittest

class TestSolution(unittest.TestCase):
    def testCountSubstrings(self):
        s = Solution()
        self.assertEqual(s.countSubstrings(s = "abc"), 3)
        self.assertEqual(s.countSubstrings(s = "aaa"), 6)
        


if __name__ == '__main__':
    unittest.main()