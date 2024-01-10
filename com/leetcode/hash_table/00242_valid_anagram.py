from typing import Dict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s or not t or len(s)!=len(t):
            return False
        d=dict()
        for c in s:
            d[c]=d[c]+1 if c in d else 1
        for c in t:
            if c not in d:
                return False
            d[c]=d[c]-1
            if d[c]<0:
                return False
        return True

import unittest

class TestSolution(unittest.TestCase):
    def testIsAnagram(self):
        s = Solution()
        self.assertEqual(s.isAnagram('anagram','nagaram'), True)
        self.assertEqual(s.isAnagram('rat','car'), False)


if __name__ == '__main__':
    unittest.main()