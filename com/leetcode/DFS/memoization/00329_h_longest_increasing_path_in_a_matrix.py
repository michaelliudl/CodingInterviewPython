from typing import List

class Solution:

    # DFS with memoization of longest increasing path at each location
    # Don't use visited we need to explore all possible paths
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        def dfs(row, col):
            if cache[row][col] > 0:
                return cache[row][col]
            curLen = 1
            for dRow, dCol in [(-1,0), (1,0), (0,-1), (0, 1)]:
                nRow, nCol = row + dRow, col + dCol
                if 0 <= nRow < rows and 0 <= nCol < cols and matrix[nRow][nCol] > matrix[row][col]:
                    result = dfs(nRow, nCol)
                    curLen = max(curLen, result + 1)
            cache[row][col] = curLen
            return curLen

        if not matrix:
            return 0
        longest = 0
        rows, cols = len(matrix), len(matrix[0])
        cache = [[0] * cols for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                result = dfs(row, col)
                longest = max(longest, result)
        return longest

import unittest

class TestSolution(unittest.TestCase):
    def testLongestIncreasingPath(self):
        s = Solution()
        self.assertEqual(s.longestIncreasingPath(matrix = [[13,5,13,9],[5,0,2,9],[10,13,11,10],[0,0,13,13]]), 6)
        self.assertEqual(s.longestIncreasingPath(matrix = [[9,9,4],[6,6,8],[2,1,1]]), 4)
        self.assertEqual(s.longestIncreasingPath(matrix = [[3,4,5],[3,2,6],[2,2,1]]), 4)
        self.assertEqual(s.longestIncreasingPath(matrix = [[1]]), 1)


if __name__ == '__main__':
    unittest.main()