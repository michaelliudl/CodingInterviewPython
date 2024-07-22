from typing import List

class Solution:

    # Set each cell to min of row sum and column sum, then subtract it from row and column sum
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                cur = min(rowSum[i], colSum[j])
                res[i][j] = cur
                rowSum[i] -= cur
                colSum[j] -= cur
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testCanJump(self):
        s = Solution()
        self.assertEqual(s.canJump(nums = [2,3,1,1,4]), True)
        self.assertEqual(s.canJump(nums = [3,2,1,0,4]), False)
        


if __name__ == '__main__':
    unittest.main()