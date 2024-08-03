from typing import List
import math, functools

class Solution:

    # Similar to # 322 Coin Change

    # Top-down recursion with memoization
    # Time O(n*`shelfWidth`), space O(n)
    def minHeightShelvesTopDown(self, books: List[List[int]], shelfWidth: int) -> int:
        
        @functools.lru_cache(maxsize=None)
        def dp(index):
            if index == len(books):
                return 0
            remWidth = shelfWidth   # Recurse from each new index starts a new shelf
            maxHeight = 0           # Max height in current shelf
            res = math.inf          # Possible min height of shelves formed by books up to `index`
            for j in range(index, len(books)):
                width, height = books[j]
                if remWidth < width:    # Not enough width, start a new shelf
                    break
                remWidth -= width
                maxHeight = max(maxHeight, height)
                res = min(res, dp(j + 1) + maxHeight)
            return res

        res = dp(index=0)
        return res if res != math.inf else -1

    # Bottom-up DP
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        dp = [0] * (len(books) + 1)
        for i in range(len(books) - 1, -1, -1):
            remWidth = shelfWidth
            maxHeight = 0
            dp[i] = math.inf
            for j in range(i, len(books)):
                width, height = books[j]
                if remWidth < width:
                    break
                remWidth -= width
                maxHeight = max(maxHeight, height)
                dp[i] = min(dp[i], dp[j + 1] + maxHeight)
        return dp[0]

import unittest

class TestSolution(unittest.TestCase):
    def testMinHeightShelves(self):
        s = Solution()
        self.assertEqual(s.minHeightShelves(books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelfWidth = 4), 6)
        self.assertEqual(s.minHeightShelves(books = [[1,3],[2,4],[3,2]], shelfWidth = 6), 4)


if __name__ == '__main__':
    unittest.main()