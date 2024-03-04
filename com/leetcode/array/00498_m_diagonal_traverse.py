from typing import List

class Solution:

    # Simulate by moving row and column index m*n times
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]: return []
        m, n = len(mat), len(mat[0])
        ans = [0] * (m * n)
        row, col, up = 0, 0, True
        for i in range(m * n):
            ans[i] = mat[row][col]
            if up:      # Move from bottom-left to up-right
                if row == 0 or col == n - 1:
                    if col == n - 1:
                        row += 1
                    else:
                        col += 1
                    up = False
                else:
                    row -= 1
                    col += 1
            else:
                if row == m - 1 or col == 0:
                    if row == m - 1:
                        col += 1
                    else:
                        row += 1
                    up = True
                else:
                    row += 1
                    col -= 1
        return ans
    
import unittest

class TestSolution(unittest.TestCase):
    def testFindDiagonalOrder(self):
        s = Solution()
        self.assertEqual(s.findDiagonalOrder(mat = [[1,2,3],[4,5,6],[7,8,9]]), [1,2,4,7,5,3,6,8,9])
        self.assertEqual(s.findDiagonalOrder(mat = [[1,2],[3,4]]), [1,2,3,4])

if __name__ == '__main__':
    unittest.main()