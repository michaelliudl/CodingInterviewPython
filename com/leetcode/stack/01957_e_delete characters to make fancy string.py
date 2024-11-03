from typing import List

class Solution:
    
    def makeFancyString(self, s: str) -> str:
        stack = []
        for char in s:
            if len(stack) > 1 and char == stack[-1] == stack[-2]:
                continue
            stack.append(char)
        return ''.join(stack)


import unittest

class TestSolution(unittest.TestCase):
    def testSimplifyPath(self):
        s = Solution()
        self.assertEqual(s.simplifyPath("/home/"), "/home")
        self.assertEqual(s.simplifyPath("/../"), "/")
        self.assertEqual(s.simplifyPath("/home//foo/"), "/home/foo")



if __name__ == '__main__':
    unittest.main()