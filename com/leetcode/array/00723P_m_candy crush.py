from typing import List

'''
This question is about implementing a basic elimination algorithm for Candy Crush.

Given an m x n integer array board representing the grid of candy where board[i][j] represents the type of candy. A value of board[i][j] == 0 represents that the cell is empty.

The given board represents the state of the game following the player's move. Now, you need to restore the board to a stable state by crushing candies according to the following rules:

If three or more candies of the same type are adjacent vertically or horizontally, crush them all at the same time - these positions become empty.
After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these candies will drop until they hit a candy or bottom at the same time. No new candies will drop outside the top boundary.
After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
If there does not exist more candies that can be crushed (i.e., the board is stable), then return the current board.
You need to perform the above rules until the board becomes stable, then return the stable board.

'''

class Solution:

    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:

        def findOnRow(toCrush, row, col):
            val = board[row][col]
            sameOnRow = set()
            sameOnRow.add(col)
            for i in range(col - 1, -1, -1):
                if board[row][i] == val:
                    sameOnRow.add(i)
                else:
                    break
            for i in range(col + 1, cols):
                if board[row][i] == val:
                    sameOnRow.add(i)
                else:
                    break
            if len(sameOnRow) >= 3:
                for i in sameOnRow:
                    toCrush.add((row, i))

        def findOnCol(toCrush, row, col):
            val = board[row][col]
            sameOnCol = set()
            sameOnCol.add(row)
            for i in range(row - 1, -1, -1):
                if board[i][col] == val:
                    sameOnCol.add(i)
                else:
                    break
            for i in range(row + 1, rows):
                if board[i][col] == val:
                    sameOnCol.add(i)
                else:
                    break
            if len(sameOnCol) >= 3:
                for i in sameOnCol:
                    toCrush.add((i, col))    

        def find():
            toCrush = set()
            for row in range(rows):
                for col in range(cols):
                    if board[row][col] != 0:
                        findOnRow(toCrush, row, col)
                        findOnCol(toCrush, row, col)
            for row, col in toCrush:
                board[row][col] = -1
            return len(toCrush)

        def crush():
            for row in range(rows):
                for col in range(cols):
                    if board[row][col] == -1:
                        if row == 0:
                            board[row][col] = 0
                            continue
                        for i in range(row, 0, -1):
                            board[i][col] = board[i - 1][col]
                        board[0][col] = 0
                    
        if not board:
            return []
        rows, cols = len(board), len(board[0])
        while True:
            toCrush = find()
            if toCrush == 0:
                break
            crush()
        return board


import unittest

class TestSolution(unittest.TestCase):

    def testCandyCrush(self):
        s=Solution()
        self.assertEqual(s.candyCrush(board = [[1,3,5,5,2],
                                               [3,4,3,3,1],
                                               [3,2,4,5,2],
                                               [2,4,4,5,5],
                                               [1,4,4,1,1]]), 
                         [[1,3,0,0,0],
                          [3,4,0,5,2],
                          [3,2,0,3,1],
                          [2,4,0,5,2],
                          [1,4,3,1,1]])
        self.assertEqual(s.candyCrush(board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]), 
                         [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]])

if __name__ == '__main__':
    unittest.main()