from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # Divide and conquer. Split by indices of matching characters and recursively check possible lengths of substring.
    def possiblyEquals(self, s1: str, s2: str) -> bool:

        def isDigit(ch):
            return '0' <= ch <= '9'
        
        def isChar(ch):
            return 'a' <= ch <= 'z'

        if not s1 and not s2:
            return True
        if not s1 or not s2:
            return False
        

import unittest

class TestSolution(unittest.TestCase):
    def testLongestSubstring(self):
        s = Solution()
        self.assertEqual(s.longestSubstring(s = "ababacb", k = 3), 0)
        self.assertEqual(s.longestSubstring(s = "ababbc", k = 2), 5)
        self.assertEqual(s.longestSubstring(s = "cababb", k = 2), 5)
        self.assertEqual(s.longestSubstring(s = "aaabb", k = 3), 3)


if __name__ == '__main__':
    unittest.main()