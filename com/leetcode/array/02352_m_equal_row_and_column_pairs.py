from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        n,ans=len(grid),0
        for i in range(n):
            for j in range(n):
                same = True
                for k in range(n):
                    if grid[i][k] != grid[k][j]:
                        same =False
                        break
                if same:
                    ans += 1
        return ans




import unittest

class TestSolution(unittest.TestCase):
    def testEqualPairs(self):
        s = Solution()
        self.assertEqual(s.equalPairs(grid = [[3,2,1],[1,7,6],[2,7,7]]), 1)
        self.assertEqual(s.equalPairs(grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]), 3)

if __name__ == '__main__':
    unittest.main()