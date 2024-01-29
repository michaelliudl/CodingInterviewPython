from typing import List

class Solution:

    # dp[i][j] is where substring s[i:j] inclusive is palindrome, default is False
    # dp[i][j] = True               If s[i]==s[j] and i==j (single char) or abs(i-j)==1 (double)
    # dp[i][j] = dp[i+1][j-1]       If s[i]==s[j] and abs(i-j)>1    (substring is palindrome or not)
    # Traverse i backwards and j forwards from i
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s
        n=len(s)
        left,right,longest=-1,-1,0          # Track longest paralindrome length and boundary
        dp=[[False]*n for i in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j]:
                    if abs(j-i)<=1:
                        dp[i][j]=True
                    else:
                        dp[i][j]=dp[i+1][j-1]
                if dp[i][j]:
                    curLen=j+1-i
                    if curLen>longest:
                        longest=curLen
                        left,right=i,j
        return s[left:right+1]
        

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
        self.assertEqual(s.longestPalindrome(s = "aacabdkacaa"), 'aca')
        self.assertEqual(s.longestPalindrome(s = "babad"), 'aba')
        self.assertEqual(s.longestPalindrome(s = "cbbd"), 'bb')
        


if __name__ == '__main__':
    unittest.main()