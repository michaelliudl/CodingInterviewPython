from typing import List

class Solution:

    # Using stack track only left parens
    def minInsertionsStack(self, s: str) -> int:
        if not s:
            return 0
        stack = []
        inserts = 0
        i = 0
        while i < len(s):
            if s[i] == '(':
                stack.append(s[i])      # Track '(' in stack
                i += 1
            else:
                if i + 1 < len(s) and s[i + 1] == ')':  # '))'
                    if stack:
                        stack.pop()                     # '())'
                    else:
                        inserts += 1                    # Need to insert 1 '(' before '))'
                    i += 2
                else:
                    if stack:
                        stack.pop()                     # '()'
                        inserts += 1                    # Pop left paren, need 1 right to pair
                    else:
                        inserts += 2                    # Need to insert 1 '(' and 1 ')'
                    i += 1
        inserts += len(stack) * 2
        return inserts

    # Counting without stack
    def minInsertions(self, s: str) -> int:
        if not s:
            return 0
        left = right = 0    # Count of left and right paren needed to make the string balance so far, increment 1 for each missing '(' or ')'
        rightNeeded = 0     # Increment by 2 for each '('
        for char in s:
            if char == '(':
                if rightNeeded % 2 == 1:    # Needed right but already obtain partial before this '(', e.g. '()('
                    right += 1
                    rightNeeded -=1
                rightNeeded += 2
            else:
                if rightNeeded == 0:        # Handles starting with ')' case
                    left += 1
                    rightNeeded += 1
                else:
                    rightNeeded -= 1
        return left + right + rightNeeded

import unittest

class TestSolution(unittest.TestCase):
    def testMinInsertions(self):
        s = Solution()
        self.assertEqual(s.minInsertions(s = "(()))"), 1)
        self.assertEqual(s.minInsertions(s = "())"), 0)
        self.assertEqual(s.minInsertions(s = "))())("), 3)



if __name__ == '__main__':
    unittest.main()