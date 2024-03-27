from typing import List

class Solution:

    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        if not mat or k == 0:
            return mat
        rows, cols = len(mat), len(mat[0])
        prefixSum = [[0] * (cols + 1) for _ in range(rows + 1)]
        # for row in range(rows):
        #     for col in range(cols):
        #         prefixSum[row + 1][col + 1] = (mat[row][col] + prefixSum[row + 1][col] + prefixSum[row][col + 1]
        #                                        - prefixSum[row][col] )
        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                prefixSum[row][col] = prefixSum[row][col - 1] + mat[row - 1][col - 1]
        for col in range(1, cols + 1):
            for row in range(1, rows + 1):
                prefixSum[row][col] += prefixSum[row - 1][col]
        result = [[0] * (cols) for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                rowMinus = max(0, row - k) + 1          # In original matrix range, +1 for prefix sum range
                colMinus = max(0, col - k) + 1
                rowPlus = min(rows - 1, row + k) + 1
                colPlus = min(cols - 1, col + k) + 1
                result[row][col] = (prefixSum[rowPlus][colPlus] + prefixSum[rowMinus - 1][colMinus - 1]
                                    - prefixSum[rowPlus][colMinus - 1] - prefixSum[rowMinus - 1][colPlus])
        return result

    def matrixBlockSum1(self, mat: List[List[int]], k: int) -> List[List[int]]:
        if not mat or k == 0:
            return mat
        rows, cols = len(mat), len(mat[0])
        for row in range(1, rows):
            for col in range(cols):
                mat[row][col] += mat[row - 1][col]
        for col in range(1, cols):
            for row in range(rows):
                mat[row][col] += mat[row][col - 1]
        # print(mat)
        result = [[0] * cols for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                rowPlus = row + k if row + k < rows else rows - 1
                rowMinus = row - k if row - k >= 0 else -1
                colPlus = col + k if col + k < cols else cols - 1
                colMinus = col - k if col - k >= 0 else -1
                # valPlus = mat[rowPlus][colPlus]
                # valMinus = 0
                # if rowMinus >= 0 and colMinus >= 0:
                #     valMinus = mat[rowMinus][colMinus]
                # elif rowMinus >= 0:
                #     valMinus = mat[rowMinus][0]
                # elif colMinus >= 0:
                #     valMinus = mat[0][colMinus]
                result[row][col] = (mat[rowPlus][rowMinus] + (mat[rowMinus][colMinus] if rowMinus >= 0 and colMinus >= 0 else 0)
                                    - (mat[rowPlus][colMinus] if colMinus >= 0 else 0)
                                    - (mat[rowMinus][colPlus] if rowMinus >= 0 else 0))
        return result

import unittest

class TestSolution(unittest.TestCase):
    def testMatrixBlockSum(self):
        s = Solution()
        self.assertEqual(s.matrixBlockSum(mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1), 
                         [[12,21,16],[27,45,33],[24,39,28]])
        self.assertEqual(s.matrixBlockSum(mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2), 
                         [[45,45,45],[45,45,45],[45,45,45]])


if __name__ == '__main__':
    unittest.main()