from typing import List

class Solution:

    # Stack to track score
    def scoreOfParentheses(self, s: str) -> int:
        if not s:
            return 0
        stack = [0]     # Add first 0 to capture total score
        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                top = stack.pop()
                if top == 0:        # () no nesting
                    stack[-1] += 1
                else:
                    stack[-1] += top * 2    # Nested parens have score as `top`
        return stack[0]


        

import unittest

class TestSolution(unittest.TestCase):
    def testScoreOfParentheses(self):
        s = Solution()
        self.assertEqual(s.scoreOfParentheses(s = "()"), 1)
        self.assertEqual(s.scoreOfParentheses(s = "(())"), 2)
        self.assertEqual(s.scoreOfParentheses(s = "()()"), 2)
        self.assertEqual(s.scoreOfParentheses(s = "(()(()))"), 6)


if __name__ == '__main__':
    unittest.main()