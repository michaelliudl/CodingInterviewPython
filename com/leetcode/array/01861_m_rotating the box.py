from typing import List
import random

class Solution:

    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        if not box:
            return box
        rows, cols = len(box), len(box[0])
        for row in range(rows):
            empty = cols
            for col in range(cols - 1, -1, -1):
                if box[row][col] == '.' and empty == cols:
                    empty = col
                if box[row][col] == '#' and empty < cols:
                    box[row][col] = '.'
                    box[row][empty] = '#'
                    empty -= 1
                if box[row][col] == '*':
                    empty = cols
        result = [[''] * rows for _ in range(cols)]
        for row in range(rows):
            for col in range(cols):
                result[col][rows - 1 - row] = box[row][col]
        return result


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