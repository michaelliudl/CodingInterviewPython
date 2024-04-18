from typing import List,Deque

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        def bfs():
            queue = Deque()
            queue.append((clickRow, clickCol))
            visited = set()
            visited.add((clickRow, clickCol))
            while queue:
                row, col = queue.popleft()
                count = 0
                neighbors = []
                for dRow, dCol in ((-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)):
                    nRow, nCol = row + dRow, col + dCol
                    if 0 <= nRow < rows and 0 <= nCol < cols and (nRow, nCol):
                        if board[nRow][nCol] == 'M':
                            count += 1
                        if board[nRow][nCol] == 'E' and (nRow, nCol) not in visited:
                            neighbors.append((nRow, nCol))
                board[row][col] = 'B' if count == 0 else str(count)
                # Only add neighbor to queue if there are no mines around current slot, per problem statement
                if count == 0:
                    for neighbor in neighbors:
                        queue.append(neighbor)
                        visited.add(neighbor)

        rows, cols = len(board), len(board[0])
        clickRow, clickCol = click
        if board[clickRow][clickCol] == 'M':
            board[clickRow][clickCol] = 'X'
            return board
        bfs()
        return board

        

import unittest

class TestSolution(unittest.TestCase):
    def testNumEnclaves(self):
        s = Solution()
        self.assertEqual(s.numEnclaves(grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]), 3)
        self.assertEqual(s.numEnclaves(grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]), 0)
        


if __name__ == '__main__':
    unittest.main()