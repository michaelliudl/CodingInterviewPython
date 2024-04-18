from typing import List

'''
Given a pattern and a string s, return true if s matches the pattern.

A string s matches a pattern if there is some bijective mapping of single characters to non-empty strings such that if each character in pattern is replaced by the string it maps to, then the resulting string is s. A bijective mapping means that no two characters map to the same string, and no character maps to two different strings.
'''

class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:

        def backtrack(patIndex, sIndex):
            if patIndex == patLen and sIndex == sLen:
                return True
            if patIndex == patLen or sIndex == sLen:
                return False
            
            char = pattern[patIndex]
            if char in patToS:
                subS = patToS[char]
                if subS != s[sIndex:(sIndex + len(subS))]:
                    return False
                return backtrack(patIndex + 1, sIndex + len(subS))
            
            patRem = patLen - patIndex - 1
            for i in range(sIndex, (sLen - patRem + 1)):
                subS = s[sIndex:i + 1]
                if subS in sToPat:
                    continue
                patToS[char] = subS
                sToPat[subS] = char
                if backtrack(patIndex + 1, i + 1):
                    return True
                del sToPat[subS]
                del patToS[char]
            return False

        if not pattern or not s or len(pattern) > len(s):
            return False
        patLen, sLen = len(pattern), len(s)
        patToS, sToPat = {}, {}
        result = backtrack(patIndex = 0, sIndex = 0)
        return result

import unittest

class TestSolution(unittest.TestCase):
    def testWordPatternMatch(self):
        s = Solution()
        self.assertEqual(s.wordPatternMatch(pattern = "abab", s = "redblueredblue"), True)
        self.assertEqual(s.wordPatternMatch(pattern = "aaaa", s = "asdasdasdasd"), True)
        self.assertEqual(s.wordPatternMatch(pattern = "aabb", s = "xyzabcxzyabc"), False)
        


if __name__ == '__main__':
    unittest.main()