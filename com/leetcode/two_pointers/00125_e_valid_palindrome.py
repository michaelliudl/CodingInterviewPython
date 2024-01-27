from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        i,j=0,len(s)-1
        while i<j:
            if not self.isAlphaNum(s[i]):
                i+=1
                continue
            if not self.isAlphaNum(s[j]):
                j-=1
                continue
            if not self.isEqual(s[i],s[j]):
                return False
            i+=1
            j-=1
        return True
    
    def isEqual(self,x,y):
        if self.isLetter(x) and self.isLetter(y):
            dx=(ord(x)-ord('A')) if self.isUpper(x) else ord(x)-ord('a')
            dy=(ord(y)-ord('A')) if self.isUpper(y) else ord(y)-ord('a')
            return dx==dy
        return x==y

    def isAlphaNum(self,c):
        return self.isLower(c) or self.isUpper(c) or self.isNum(c)
    
    def isLetter(self,c):
        return self.isLower(c) or self.isUpper(c)

    def isLower(self,c):
        return c>='a' and c<='z'
    
    def isUpper(self,c):
        return c>='A' and c<='Z'

    def isNum(self,c):
        return c>='0' and c<='9'

import unittest

class TestSolution(unittest.TestCase):
    def testIsPalindrome(self):
        s = Solution()
        self.assertEqual(s.isPalindrome(s = "A man, a plan, a canal: Panama"), True)
        self.assertEqual(s.isPalindrome(s = "race a car"), False)
        self.assertEqual(s.isPalindrome(" "), True)


if __name__ == '__main__':
    unittest.main()