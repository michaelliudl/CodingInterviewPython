from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # Divide and conquer. Split by indices of characters not having >= k occurrences and recursively search in substrings
    def longestSubstring(self, s: str, k: int) -> int:

        def recur(left, right):
            nonlocal ans
            countMap,indexMap = {},{}
            for i in range(left,right):
                c = s[i]
                countMap[c] = countMap.get(c, 0) + 1
                if c not in indexMap:
                    indexMap[c] = []
                indexMap[c].append(i)
            lessThanKIndices = []
            for c,count in countMap.items():
                if count < k:
                    for index in indexMap[c]:
                        lessThanKIndices.append(index)
            if not lessThanKIndices:
                ans = max(ans, (right - left))
                return
            lessThanKIndices.sort()
            start = left
            for index in lessThanKIndices:
                recur(start, index)
                start = index + 1
            recur(start, right)

        if not s: return 0
        n = len(s)
        ans = 0
        recur(0, n)
        return ans

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