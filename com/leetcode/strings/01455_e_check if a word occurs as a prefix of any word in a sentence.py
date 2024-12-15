from typing import List

class Solution:

    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, word in enumerate(sentence.split()):
            if word.startswith(searchWord):
                return i + 1
        return -1


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