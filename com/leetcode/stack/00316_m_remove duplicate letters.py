from typing import List

class Solution:

    # Note last index of each unique char
    # Use stack to add chars, skip if it's already added
    # If first time adding a smaller char, and current index is less than the last index of top of stack char, keep popping out top of stack and remove popped char from `added` set
    # Same as 1081
    def removeDuplicateLetters(self, s: str) -> str:
        if not s:
            return s
        charLastIndex = {}
        for index, char in enumerate(s):
            charLastIndex[char] = index
        stack = []
        added = set()
        for index, char in enumerate(s):
            if char in added:
                continue
            while stack and char < stack[-1] and index < charLastIndex[stack[-1]]:
                popped = stack.pop()
                added.remove(popped)
            stack.append(char)
            added.add(char)
        return ''.join(stack)


import unittest

class TestSolution(unittest.TestCase):
    pass



if __name__ == '__main__':
    unittest.main()