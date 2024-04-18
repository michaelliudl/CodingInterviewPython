from typing import List,Deque

class Solution:

    # Count
    def checkValidString(self, s: str) -> bool:
        low = high = 0
        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                if low > 0:
                    low -= 1
                high -= 1
            else:
                if low > 0:
                    low -= 1
                high += 1
            if high < 0:
                return False
        return low == 0

    # Stack and queue
    def checkValidStringStack(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        star = Deque()                      # Keep `*` index
        for index, char in enumerate(s):
            if char == '*':
                star.append(index)
            elif char == '(':
                stack.append((char, index)) # '(' and index
            else:
                if not stack and not star:  # No way to pair a ')'
                    return False
                elif stack and stack[-1][0] == '(':
                    stack.pop()
                else:
                    star.popleft()          # Pair ')' with left most `*`
        if len(stack) == 0:                 # Parens paired
            return True
        if len(star) < len(stack):          # Not enough `*` to pair with remaining '('
            return False
        for i in range(len(stack) - 1, -1, -1):     # '(' can only be paired with a `*` if its index is before star's index
            if not star or star[-1] < stack[i][1]:
                return False
            star.pop()
        return True

import unittest

class TestSolution(unittest.TestCase):
    def testCheckValidString(self):
        s = Solution()
        self.assertEqual(s.checkValidString(s = "*(()"), False)
        self.assertEqual(s.checkValidString(s = "()"), True)
        self.assertEqual(s.checkValidString(s = "(*)"), True)
        self.assertEqual(s.checkValidString(s = "(*))"), True)
        self.assertEqual(s.checkValidString(s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"), False)
        
if __name__ == '__main__':
    unittest.main()