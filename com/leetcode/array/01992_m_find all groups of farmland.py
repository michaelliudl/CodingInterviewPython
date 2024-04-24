from typing import List

class Solution:

    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:

        def corner(x, y):
            nx, ny = x, y
            while nx + 1 < m and land[nx + 1][y] == 1:
                nx += 1
            while ny + 1 < n and land[x][ny + 1] == 1:
                ny += 1
            for i in range(x, nx + 1):
                for j in range(y, ny + 1):
                    land[i][j] = 2
            return [nx, ny]

        if not land:
            return []
        ret = []
        m, n = len(land), len(land[0])
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    farm = [i, j]
                    farm.extend(corner(i, j))
                    ret.append(farm)
        return ret


        

import unittest

class TestSolution(unittest.TestCase):

    def testSortedSquares(self):
        s = Solution()
        self.assertEqual(s.minCost(colors = "aaabbbabbbb", neededTime = [3,5,10,7,5,3,5,5,4,8,1]), 26)
        self.assertEqual(s.minCost(colors = "abaac", neededTime = [1,2,3,4,5]), 3)
        self.assertEqual(s.minCost(colors = "abc", neededTime = [1,2,3]), 0)
        self.assertEqual(s.minCost(colors = "aabaa", neededTime = [1,2,3,4,1]), 2)

if __name__ == '__main__':
    unittest.main()