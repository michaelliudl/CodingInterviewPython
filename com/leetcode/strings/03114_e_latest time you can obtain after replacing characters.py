from typing import List

class Solution:

    def findLatestTime(self, s: str) -> str:
        sList = list(s)
        # Hour
        if sList[0] == '?':
            if sList[1] in ('?', '0', '1'):
                sList[0] = '1'
            else:
                sList[0] = '0'
        if sList[1] == '?':
            if sList[0] in ('?', '1'):
                sList[1] = '1'
            else:
                sList[1] = '9'
        # Minute
        if sList[3] == '?':
            sList[3] = '5'
        if sList[4] == '?':
            sList[4] = '9'
        return ''.join(sList)


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