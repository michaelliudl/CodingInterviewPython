from typing import List

class Solution:

    # Greedy
    # 1. Flip row if first number is 0
    # 2. Flip col if it has more 0s than 1s
    def matrixScore(self, grid: List[List[int]]) -> int:

        def flipRow(i):
            for j in range(n):
                grid[i][j] = 1 if grid[i][j] == 0 else 0
        
        def flipCol(j):
            for i in range(m):
                grid[i][j] = 1 if grid[i][j] == 0 else 0

        m, n = len(grid), len(grid[0])
        for i in range(m):
            if grid[i][0] == 0:
                flipRow(i)
        for j in range(n):
            zeros = 0
            for i in range(m):
                if grid[i][j] == 0:
                    zeros += 1
            if zeros > (m - zeros):
                flipCol(j)
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += (1 << n - 1 - j)
        return res


import unittest

class TestSolution(unittest.TestCase):
    def testCanJump(self):
        s = Solution()
        self.assertEqual(s.canJump(nums = [2,3,1,1,4]), True)
        self.assertEqual(s.canJump(nums = [3,2,1,0,4]), False)
        


if __name__ == '__main__':
    unittest.main()