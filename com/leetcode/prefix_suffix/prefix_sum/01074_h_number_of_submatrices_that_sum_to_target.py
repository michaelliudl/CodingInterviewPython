from typing import List

class Solution:

    # Calculate prefix sum for each row
    # Iterate all combination of columns and use prefix sum diff to calculate submatrix sum
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        if not matrix: return 0
        m,n,r=len(matrix),len(matrix[0]),0

        # Update matrix columns to prefix sum in each row
        for i in range(m):
            for j in range(1,n):
                matrix[i][j] += matrix[i][j-1]

        for i in range(n):
            for j in range(i,n):
                count_map={0: 1}            # Map to count subarrays with given sum
                current_sum = 0
                for k in range(m):
                    if i==0:
                        current_sum += matrix[k][j]
                    else:
                        current_sum += matrix[k][j] - matrix[k][i-1]
                    diff = current_sum - target
                    if diff in count_map:
                        r += count_map[diff]
                    if current_sum in count_map:
                        count_map[current_sum]+=1
                    else:
                        count_map[current_sum]=1
        return r

import unittest

class TestSolution(unittest.TestCase):
    def testNumSubmatrixSumTarget(self):
        s = Solution()
        self.assertEqual(s.numSubmatrixSumTarget(matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0), 4)
        self.assertEqual(s.numSubmatrixSumTarget(matrix = [[1,-1],[-1,1]], target = 0), 5)
        self.assertEqual(s.numSubmatrixSumTarget(matrix = [[904]], target = 0), 0)
        


if __name__ == '__main__':
    unittest.main()