from typing import List

class Solution:

    def myAtoi(self, s: str) -> int:
        signFound = False
        positive = True
        numStart = -1
        numEnd = -1
        for i, char in enumerate(s):
            if char < '0' or char > '9':
                if numStart < 0:
                    if char not in (' ', '+', '-') or signFound:
                        break
                    elif char in ('+', '-'):
                        if signFound:
                            break
                        positive = char == '+'
                        signFound = True
                else:
                    numEnd = i
                    break
            elif numStart < 0:
                numStart = i
        if numStart >= 0 and numEnd < 0:
            numEnd = len(s)
        if 0 <= numStart <= numEnd:
            result = 0
            for i in range(numStart, numEnd):
                result = result * 10 + (ord(s[i]) - ord('0'))
            if positive:
                return result if result <= 2**31 - 1 else 2**31 - 1
            else:
                result = -1 * result
                return result if result >= -2**31 else -2**31
        return 0

    def myAtoi1(self, s: str) -> int:
        if not s: return 0
        ans = 0
        signValid, negative = True, False
        for c in s:
            if c == ' ':
                if signValid:
                    continue
                else:
                    break
            if (c < '0' or c > '9') and c not in ('+','-'):
                break
            if c in ('+','-'):
                if signValid:
                    signValid = False
                    negative = True if c == '-' else False
                else:
                    break
            if c >= '0' and c <= '9':
                signValid = False
                ans = ans * 10 + int(c)
        if negative: ans = -ans
        if ans < -2**31: ans = -2**31
        if ans > 2**31-1: ans = 2**31-1
        return ans
    
                       


import unittest

class TestSolution(unittest.TestCase):
    def testMyAtoi(self):
        s = Solution()
        self.assertEqual(s.myAtoi(s = "   +0 123"), 0)
        self.assertEqual(s.myAtoi(s = "00000-42a1234"), 0)
        self.assertEqual(s.myAtoi(s = "   -42"), -42)
        self.assertEqual(s.myAtoi(s = "42"), 42)
        self.assertEqual(s.myAtoi(s = "+-12"), 0)
        self.assertEqual(s.myAtoi(s = "words and 987"), 0)
        self.assertEqual(s.myAtoi(s = "4193 with words"), 4193)
        

if __name__ == '__main__':
    unittest.main()