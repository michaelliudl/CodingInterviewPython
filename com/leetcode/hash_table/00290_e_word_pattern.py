from typing import List

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if not pattern or not s:
            return False
        sl=s.split(' ')
        m,n=len(pattern),len(sl)
        if m!=n: return False
        d,d1={},{}          # Same key can be mapped to different words. Mapping is two way check.
        for i in range(n):
            p=pattern[i]
            w=sl[i]
            if not p in d:
                d[p]=w
            if not w in d1:
                d1[w]=p
            if d[p]!=w or d1[w]!=p:
                return False
        return True

import unittest

class TestSolution(unittest.TestCase):
    def testWordPattern(self):
        s = Solution()
        self.assertEqual(s.wordPattern(pattern = "abc", s = "b c a"), True)
        self.assertEqual(s.wordPattern(pattern = "abba", s = "dog dog dog dog"), False)
        self.assertEqual(s.wordPattern(pattern = "abba", s = "dog cat cat dog"), True)
        self.assertEqual(s.wordPattern(pattern = "abba", s = "dog cat cat fish"), False)
        self.assertEqual(s.wordPattern(pattern = "aaaa", s = "dog cat cat dog"), False)
        


if __name__ == '__main__':
    unittest.main()