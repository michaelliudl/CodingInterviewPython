from typing import List

class Solution:

    # Using stack to track start index of valid paren substring
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        maxLen = 0
        stack = [-1]        # Use `-1` as boundary if valid paren substring starts from first character
        for index, ch in enumerate(s):
            if ch == '(':
                stack.append(index)
            else:               # `ch` is `)`
                if stack[-1] > -1 and s[stack[-1]] == '(':
                    stack.pop()
                    if stack:
                        maxLen = max(maxLen, (index - stack[-1]))
                else:
                    stack.append(index)
        return maxLen



import unittest

class TestSolution(unittest.TestCase):
    def testLongestValidParentheses(self):
        s = Solution()
        self.assertEqual(s.longestValidParentheses(s = "(()"), 2)
        self.assertEqual(s.longestValidParentheses(s = ")()())"), 4)
        self.assertEqual(s.longestValidParentheses(s = ""), 0)
        self.assertEqual(s.longestValidParentheses(s = "()(()"), 2)
        


if __name__ == '__main__':
    unittest.main()