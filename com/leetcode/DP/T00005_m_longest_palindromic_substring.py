from typing import List

class Solution:

    # dp[i][j] is length of longest panlindrome of substring s[i:j] inclusive
    # dp[i][j] = dp[i+1][j-1] if s[i]==s[j]     By traverse i backwards and j forwards from i
    # dp[i][j] = max(dp[i+1][j], dp[i][j-1]) if s[i]!=s[j]
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s
        n=len(s)
        dp=[[0]*n for i in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if i==j:
                    dp[i][j]=1
                elif s[i]==s[j]:
                    dp[i][j]=dp[i+1][j-1]+2
                else:
                    dp[i][j]=max(dp[i+1][j], dp[i][j-1])
        longest=dp[0][n-1]
        for i in range(n):
            for j in range(0,i+1):
                if dp[i][i+j]==longest:
                    return s[i:j+1]
        

    def longestPalindromeTwoPointer(self, s: str) -> str:
        if not s:
            return s
        r,lr,n=s[0],1,len(s)
        for i in range(n):
            a,b=i,i
            lcur=0
            while a>=0 and b<n:
                if s[a]==s[b]:
                    lcur+=1 if a==b else 2
                    if lcur>lr:
                        lr=lcur
                        r=s[a:b+1]
                    a-=1
                    b+=1
                else:
                    break
            if i<n-1:
                a,b=i,i+1
                lcur=0
                while a>=0 and b<n:
                    if s[a]==s[b]:
                        lcur+=2
                        if lcur>lr:
                            lr=lcur
                            r=s[a:b+1]
                        a-=1
                        b+=1
                    else:
                        break
        return r



import unittest

class TestSolution(unittest.TestCase):
    def testLongestPalindrome(self):
        s = Solution()
        self.assertEqual(s.longestPalindrome(s = "babad"), 'bab')
        self.assertEqual(s.longestPalindrome(s = "cbbd"), 'bb')
        


if __name__ == '__main__':
    unittest.main()