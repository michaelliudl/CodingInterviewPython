from typing import List

class Solution:

    # Simulate
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces.sort()
        res = []
        j = 0
        for i, char in enumerate(s):
            if j < len(spaces) and i == spaces[j]:
                res.append(' ')
                j += 1
            res.append(s[i])
        return ''.join(res)

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