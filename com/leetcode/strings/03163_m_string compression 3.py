from typing import List

class Solution:

    def compressedString(self, word: str) -> str:
        comp = ''
        cur = word[0]
        left = 0
        for i in range(1, len(word)):
            if word[i] == cur and (i - left) < 9:
                continue
            comp += str(i - left)
            comp += cur
            cur = word[i]
            left = i
        comp += str(len(word) - left)
        comp += cur
        return comp

import unittest

class TestSolution(unittest.TestCase):
    def testMyAtoi(self):
        s = Solution()
        self.assertEqual(s.myAtoi(s = "   +0 123"), 0)
        self.assertEqual(s.myAtoi(s = "00000-42a1234"), 0)
        self.assertEqual(s.myAtoi(s = "   -42"), -42)
        self.assertEqual(s.myAtoi(s = "42"), 42)
        self.assertEqual(s.myAtoi(s = "+-12"), 0)
        self.assertEqual(s.myAtoi(s = "words and 987"), 0)
        self.assertEqual(s.myAtoi(s = "4193 with words"), 4193)
        

if __name__ == '__main__':
    unittest.main()