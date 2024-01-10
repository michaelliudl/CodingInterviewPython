from typing import List

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if not ransomNote or not magazine or len(ransomNote)>len(magazine):
            return False
        dr=self.strToDict(ransomNote)
        dm=self.strToDict(magazine)
        for rc in dr.keys():
            if not rc in dm or dr[rc]>dm[rc]:
                return False
        return True
        
    def strToDict(self, s: str) -> dict:
        d=dict()
        for c in s:
            d[c]=d[c]+1 if c in d else 1
        return d

import unittest

class TestSolution(unittest.TestCase):
    def testCanConstruct(self):
        s = Solution()
        self.assertEqual(s.canConstruct("a","b"), False)
        self.assertEqual(s.canConstruct("aa","ab"), False)
        self.assertEqual(s.canConstruct("aa","aab"), True)


if __name__ == '__main__':
    unittest.main()