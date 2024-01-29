from typing import List

class Solution:

    def isLongPressedName(self, name: str, typed: str) -> bool:
        if not name or not typed or len(name)>len(typed): return False
        i,j=0,0
        while j<len(typed):
            if i<len(name) and name[i]==typed[j]:
                i+=1
                j+=1
            elif j>0 and typed[j]==typed[j-1]:
                j+=1
            else:
                return False
        return i==len(name)


import unittest

class TestSolution(unittest.TestCase):
    def testIsLongPressedName(self):
        s = Solution()
        self.assertEqual(s.isLongPressedName(name = "alex", typed = "aaleexx"), True)
        self.assertEqual(s.isLongPressedName(name = "alex", typed = "aaleexxxxx"), True)
        self.assertEqual(s.isLongPressedName(name = "saeed", typed = "ssaaedd"), False)
        self.assertEqual(s.isLongPressedName(name = "leelee", typed = "lleeelee"), True)
        self.assertEqual(s.isLongPressedName(name = "alex", typed = "aaleexabc"), False)
        self.assertEqual(s.isLongPressedName(name = "alexabc", typed = "aaleexxxxxx"), False)


if __name__ == '__main__':
    unittest.main()