from typing import List

class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n     # Track each row, column, diag and anti-diag values
        self.cols = [0] * n
        self.diag = 0
        self.antiDiag = 0
        # self.grid = [[0] * n for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        value = 1 if player == 1 else -1
        target = self.n if player == 1 else -self.n

        if row == col:                  # Played on diag
            self.diag += value
            if self.diag == target:
                return player
            
        if row + col == self.n - 1:     # Played on anti-diag
            self.antiDiag += value
            if self.antiDiag == target:
                return player
        
        self.rows[row] += value
        if self.rows[row] == target:
            return player
        
        self.cols[col] += value
        if self.cols[col] == target:
            return player
        return 0
    
    # Brute
    def moveWithGrid(self, row: int, col: int, player: int) -> int:

        def check():
            for row in self.grid:
                sumRow = sum(row)
                if sumRow == self.n:
                    return 1
                elif sumRow == -self.n:
                    return 2
            for col in range(self.n):
                sumCol = sum(row[col] for row in self.grid)
                if sumCol == self.n:
                    return 1
                elif sumCol == -self.n:
                    return 2
            diag1 = diag2 = 0
            for i in range(self.n):
                diag1 += self.grid[i][i]
                diag2 += self.grid[i][self.n - 1 - i]
            if diag1 == self.n or diag2 == self.n:
                return 1
            if diag1 == -self.n or diag2 == -self.n:
                return 2
            return 0

        self.grid[row][col] = 1 if player == 1 else -1
        return check()
        

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

class Solution:
    pass

import unittest

class TestSolution(unittest.TestCase):
    def testTicTacToe(self):
        t = TicTacToe(3)
        self.assertEqual(t.move(0, 0, 1), 0)
        self.assertEqual(t.move(0, 2, 2), 0)
        self.assertEqual(t.move(2, 2, 1), 0)
        self.assertEqual(t.move(1, 1, 2), 0)
        self.assertEqual(t.move(2, 0, 1), 0)
        self.assertEqual(t.move(1, 0, 2), 0)
        self.assertEqual(t.move(2, 1, 1), 1)


if __name__ == '__main__':
    unittest.main()