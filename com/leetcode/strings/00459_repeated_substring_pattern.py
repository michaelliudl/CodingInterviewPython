from typing import List

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s or len(s)<=1:
            return False
        for i in range(1,int(len(s)/2)+1):
            if len(s)%i==0:
                prefix=s[:i]
                if prefix*int(len(s)/i)==s:
                    return True
        return False

import unittest

class TestSolution(unittest.TestCase):
    def testRepeatedSubstringPattern(self):
        s = Solution()
        self.assertEqual(s.repeatedSubstringPattern("abab"), True)
        self.assertEqual(s.repeatedSubstringPattern("aba"), False)
        self.assertEqual(s.repeatedSubstringPattern("abcabcabcabc"), True)


if __name__ == '__main__':
    unittest.main()