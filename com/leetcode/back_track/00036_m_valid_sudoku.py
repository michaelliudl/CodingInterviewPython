from typing import List

class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def validRows(board):
            for _,v in enumerate(board):
                if not valid(v):
                    return False
            return True

        def valid(row):
            flag=[0]*(len(row)+1)
            for _,v in enumerate(row):
                if v!='.':
                    ele=int(v)
                    if flag[ele]:
                        return False
                    flag[ele]=1
            return True

        def validCols(board):
            for i in range(len(board)):
                if not valid([r[i] for r in board]):
                    return False
            return True

        def validSubs(board):
            for i in range(0, len(board), 3):
                for j in range(0, len(board), 3):
                    if not valid([board[x][y] for x in range(i,i+3) for y in range(j,j+3)]):
                        return False
            return True
        
        if not board or len(board)!=9 or len(board[0])!=9:
            return False
        if not validRows(board):
            return False
        if not validCols(board):
            return False
        if not validSubs(board):
            return False
        return True




import unittest

class TestSolution(unittest.TestCase):
    def testIsValidSudoku(self):
        s = Solution()
#         self.assertEqual(s.isValidSudoku(board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]), True)
        self.assertEqual(s.isValidSudoku([[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]), False)
        


if __name__ == '__main__':
    unittest.main()