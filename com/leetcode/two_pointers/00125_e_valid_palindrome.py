from typing import List

class Solution:

    def isPalindromeArrayCopy(self, s: str) -> bool:

        def valid(ch):
            return lower(ch) or upper(ch) or number(ch)
        
        def number(ch):
            return '0' <= ch <= '9'

        def lower(ch):
            return 'a' <= ch <= 'z'
        
        def upper(ch):
            return 'A' <= ch <= 'Z'

        if not s:
            return True
        array = []
        for _, ch in enumerate(s):
            if valid(ch):
                if number(ch) or lower(ch):
                    array.append(ch)
                else:
                    array.append(ch.lower())
        if not array:
            return True
        low, high = 0, len(array) - 1
        while low < high:
            if array[low] != array[high]:
                return False
            low += 1
            high -= 1
        return True

    def isPalindrome(self, s: str) -> bool:

        def valid(ch):
            return lower(ch) or upper(ch) or number(ch)
        
        def number(ch):
            return '0' <= ch <= '9'

        def lower(ch):
            return 'a' <= ch <= 'z'
        
        def upper(ch):
            return 'A' <= ch <= 'Z'

        def match(ch1, ch2):
            if (number(ch1) and not number(ch2)) or (not number(ch1) and number(ch2)):
                return False
            if number(ch1) and number(ch2):
                return int(ch1) == int(ch2)
            diff1 = ord(ch1) - (ord('A') if upper(ch1) else ord('a'))
            diff2 = ord(ch2) - (ord('A') if upper(ch2) else ord('a'))
            return diff1 == diff2

        if not s:
            return True
        low, high = 0, len(s) - 1
        while low < high:
            while low < len(s) and not valid(s[low]):
                low += 1
            while high >= 0 and not valid(s[high]):
                high -= 1
            if low > high:
                break
            if not match(s[low], s[high]):
                return False
            low += 1
            high -= 1
        return True


    def isPalindrome1(self, s: str) -> bool:
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