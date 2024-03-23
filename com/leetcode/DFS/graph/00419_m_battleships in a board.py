from typing import List

class Solution:

    # Same as number of islands if BFS/DFS
    # O(mn) and O(1) space solution is to check if left or up of 'X' is empty.
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board:
            return 0
        count = 0
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'X':      # Part of battleship
                    if ((row == 0 or board[row - 1][col] == '.') and    # Up is empty
                        (col == 0 or board[row][col - 1] == '.')):      # Left is empty
                        count += 1          # Start of battleship
        return count

import unittest

class TestSolution(unittest.TestCase):
    def testExist(self):
        s = Solution()
        self.assertEqual(s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"), True)
        self.assertEqual(s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"), True)
        self.assertEqual(s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"), False)


if __name__ == '__main__':
    unittest.main()