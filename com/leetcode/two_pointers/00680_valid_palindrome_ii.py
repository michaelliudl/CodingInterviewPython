from typing import List

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s:
            return False
        if len(s)<=1:
            return True
        i,j=0,len(s)-1
        while i<j:
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                return self.isPal(s,i+1,j) or self.isPal(s,i,j-1)
        return True
    
    def isPal(self, s: str, b: int, e: int) -> bool:
        i,j=b,e
        while i<j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True

import unittest

class TestSolution(unittest.TestCase):
    def testValidPalindrome(self):
        s = Solution()
        self.assertEqual(s.validPalindrome("aba"), True)
        self.assertEqual(s.validPalindrome("abca"), True)
        self.assertEqual(s.validPalindrome("abc"), False)
        self.assertEqual(s.validPalindrome("deeee"), True)


if __name__ == '__main__':
    unittest.main()