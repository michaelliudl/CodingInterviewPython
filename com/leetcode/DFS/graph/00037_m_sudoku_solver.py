from typing import List

class Solution:

    # Simplify code, TODO debug this time out
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def valid(row, col, option):
            for i in range(n):
                if i != row and board[i][col] == option:
                    return False
            for i in range(n):
                if i != col and board[row][i] == option:
                    return False
            rowStart = (row // 3) * 3
            colStart = (col // 3) * 3
            for i in range(rowStart, rowStart + 3):
                for j in range(colStart, colStart + 3):
                    if (i != row or j != col) and board[i][j] == option:
                        return False
            return True

        def dfs():
            for row in range(n):
                for col in range(n):
                    if board[row][col] == '.':
                        continue
                    for i in range(n):
                        option = str(i + 1)
                        if valid(row, col, option):
                            board[row][col] = option
                            result = dfs()
                            if result:
                                return True
                            board[row][col] = '.'
                    return False
            return True

        if not board or len(board) != 9 or len(board[0]) != 9:
            return
        n = len(board)
        dfs()

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def backtrack(board, n) -> bool:
            for row in range(n):
                for col in range(n):
                    if board[row][col]!='.':
                        continue
                    for k in range(n):
                        candidate=str(k+1)
                        if self.valid(board, n, row, col, candidate):
                            board[row][col]=candidate
                            r=backtrack(board, n)
                            if r:
                                return True
                            board[row][col]='.'
                    return False
            return True
        
        if not board or len(board)!=9 or len(board[0])!=9:
            return
        backtrack(board, len(board))
    
    def valid(self, board, n, row, col, candidate):
            # valid row
            for i in range(n):
                if i!=col and board[row][i]==candidate:
                    return False
            # valid column
            for i in range(n):
                if i!=row and board[i][col]==candidate:
                    return False
            # valid 3x3
            rowStart,colStart=(row//3)*3,(col//3)*3
            for rowSub in range(rowStart, rowStart+3):
                for colSub in range(colStart, colStart+3):
                    if candidate==board[rowSub][colSub] and (rowSub!=row or colSub!=col):
                        return False
            return True

import unittest

class TestSolution(unittest.TestCase):
    def testSubsets(self):
        s = Solution()
        board=[["5","3","1",    ".","7",".",    ".",".","."],
               ["6",".",".",    "1","9","5",    ".",".","."],
               [".","9","8",    ".",".",".",    ".","6","."],

               ["8",".",".",    ".","6",".",    ".",".","3"],
               ["4",".",".",    "8",".","3",    ".",".","1"],
               ["7",".",".",    ".","2",".",    ".",".","6"],

               [".","6",".",    ".",".",".",    "2","8","."],
               [".",".",".",    "4","1","9",    ".",".","5"],
               [".",".",".",    ".","8",".",    ".","7","9"]]
        self.assertEqual(s.valid(board, n=9, row=0, col=3, candidate='1'), False)

        board=[["5","3","1",    ".","7",".",    ".",".","."],
               ["6",".",".",    "1","9","5",    ".",".","."],
               [".","9","8",    ".",".",".",    ".","6","."],

               ["8",".",".",    ".","6",".",    ".",".","3"],
               ["4",".",".",    "8",".","3",    ".",".","1"],
               ["7",".",".",    ".","2",".",    ".",".","6"],
               
               [".","6",".",    ".",".",".",    "2","8","."],
               [".",".",".",    "4","1","9",    ".",".","5"],
               [".",".",".",    ".","8",".",    ".","7","9"]]
        self.assertEqual(s.valid(board, n=9, row=3, col=3, candidate='2'), False)

        board=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
        s.solveSudoku(board)
        self.assertEqual(board, [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]])
        


if __name__ == '__main__':
    unittest.main()