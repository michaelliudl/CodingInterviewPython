from typing import List
import random

class Solution:

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def liveNeighbors(i, j):
            neighbors = 0
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if 0 <= x < m and 0 <= y < n and (x != i or y != j):
                        if board[x][y] % 2 == 1:    # Live in prev round
                            neighbors += 1
            return neighbors

        if not board:
            return
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                neighbors = liveNeighbors(i, j)
                if board[i][j] == 1:
                    if neighbors < 2 or neighbors > 3:
                        board[i][j] = 3                 # 3 mean live -> die, 1 -> 0
                else:
                    if neighbors == 3:
                        board[i][j] = 2                # 2 mean die -> live, 0 -> 1
        for i in range(m):
            for j in range(n):
                if board[i][j] == 3:
                    board[i][j] = 0
                if board[i][j] == 2:
                    board[i][j] = 1


import unittest

class TestSolution(unittest.TestCase):

    def testGameOfLife(self):
        s=Solution()
        board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
        s.gameOfLife(board)
        self.assertEqual(board, [[0,0,0],[1,0,1],[0,1,1],[0,1,0]])

        board = [[1,1],[1,0]]
        s.gameOfLife(board)
        self.assertEqual(board, [[1,1],[1,1]])

if __name__ == '__main__':
    unittest.main()