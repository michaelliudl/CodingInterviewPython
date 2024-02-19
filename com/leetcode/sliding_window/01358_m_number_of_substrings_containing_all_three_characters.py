from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        if not s or len(s)<3: return 0
        curMap = {}
        left,curCount,ans = 0,0,0
        for c in s:
            if c not in curMap:
                curMap[c] = 1
                curCount += 1
            else:
                curMap[c] += 1
            while curCount == 3:
                winOut = s[left]
                curMap[winOut] -= 1
                if curMap[winOut] == 0:
                    del curMap[winOut]
                    curCount -= 1
                left += 1
            # When window closes, all substrings starting from 0 to left-1 meet requirements
            ans += left
        return ans



import unittest

class TestSolution(unittest.TestCase):
    def testNumberOfSubstrings(self):
        s = Solution()
        self.assertEqual(s.numberOfSubstrings(s = "abcabc"), 10)
        self.assertEqual(s.numberOfSubstrings(s = "aaacb"), 3)
        self.assertEqual(s.numberOfSubstrings(s = "abc"), 1)


if __name__ == '__main__':
    unittest.main()