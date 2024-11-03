from typing import List

class Solution:

    def maxUniqueSplit(self, s: str) -> int:

        def dfs(start):
            nonlocal res
            if start == len(s):
                res = max(res, len(visited))
                return
            for i in range(start, len(s)):
                subString = s[start:(i + 1)]
                if subString in visited:
                    continue
                visited.add(subString)
                dfs(start=(i + 1))
                visited.remove(subString)

        res = 0
        visited = set()
        dfs(start=0)
        return res

import unittest

class TestSolution(unittest.TestCase):

    def testMaxUniqueSplit(self):
        s = Solution()
        self.assertEqual(s.maxUniqueSplit(s = "ababccc"), 5)
        self.assertEqual(s.maxUniqueSplit(s = "aba"), 2)
        self.assertEqual(s.maxUniqueSplit(s = "aa"), 1)

if __name__ == '__main__':
    unittest.main()