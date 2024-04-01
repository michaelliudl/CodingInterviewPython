from typing import List

class Solution:

    # Note last index of each unique char
    # Use stack to add chars, skip if it's already added
    # If first time adding a smaller char, and current index is less than the last index of top of stack char, keep popping out top of stack and remove popped char from `added` set
    # Same as 316
    def smallestSubsequence(self, s: str) -> str:
        if not s:
            return s
        lastIndex = {}
        for i, char in enumerate(s):
            lastIndex[char] = i
        stack = []
        for i, char in enumerate(s):
            # Checking char in stack will be slower than using a `added` set.
            if char not in stack:
                while stack and char < stack[-1] and i < lastIndex[stack[-1]]:
                    stack.pop()
                stack.append(char)
        return ''.join(stack)


import unittest

class TestSolution(unittest.TestCase):
    pass



if __name__ == '__main__':
    unittest.main()