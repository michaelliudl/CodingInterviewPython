from typing import List

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for char in s:
            stack.append(char)
            if len(stack) > 1 and stack[len(stack) - 2:] == ['(', ')']:
                stack.pop()
                stack.pop()
        return len(stack)

import unittest

class TestSolution(unittest.TestCase):
    def testMinAddToMakeValid(self):
        s = Solution()
        self.assertEqual(s.minAddToMakeValid("())"), 1)
        self.assertEqual(s.minAddToMakeValid("((("), 3)


if __name__ == '__main__':
    unittest.main()