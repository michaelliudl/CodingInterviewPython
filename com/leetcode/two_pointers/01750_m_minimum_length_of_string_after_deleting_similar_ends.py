from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minimumLength(self, s: str) -> int:
        if not s:
            return 0
        low, high = 0, len(s) - 1
        while low < high:
            if s[low] != s[high]:
                break
            cur = s[low]
            while low <= high and s[low] == cur:
                low += 1
            while low <= high and s[high] == cur:
                high -= 1
        return high - low + 1

import unittest

class TestSolution(unittest.TestCase):
    def testMinimumLength(self):
        s = Solution()
        self.assertEqual(s.minimumLength(s = "aaaabaa"), 1)
        self.assertEqual(s.minimumLength(s = "aaaaaaa"), 0)
        self.assertEqual(s.minimumLength(s = "aaaaaa"), 0)
        self.assertEqual(s.minimumLength(s = "ca"), 2)
        self.assertEqual(s.minimumLength(s = "cabaabac"), 0)
        self.assertEqual(s.minimumLength(s = "aabccabba"), 3)


if __name__ == '__main__':
    unittest.main()