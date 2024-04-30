from typing import List

class Solution:

    def numberOfSpecialChars(self, word: str) -> int:
        low = [0]*26
        high = [0]*26
        for char in word:
            if 'a' <= char <= 'z':
                low[ord(char) - ord('a')] += 1
            if 'A' <= char <= 'Z':
                high[ord(char) - ord('A')] += 1
        return sum(1 if low[i] > 0 and high[i] > 0 else 0 for i in range(26))

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