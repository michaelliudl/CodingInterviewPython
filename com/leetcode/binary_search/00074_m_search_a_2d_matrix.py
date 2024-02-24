from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        m,n = len(matrix),len(matrix[0])
        low,high,targetRow = 0,m,-1
        while low<high:
            mid = low + (high-low) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][n-1]:
                targetRow = mid
                break
            elif target < matrix[mid][0]:
                high = mid
            else:
                low = mid + 1
        if targetRow == -1: return False
        low,high = 0,n
        while low<high:
            mid = low + (high-low) // 2
            if target == matrix[targetRow][mid]:
                return True
            elif target < matrix[targetRow][mid]:
                high = mid
            else:
                low = mid+1
        return False
            

import unittest

class TestSolution(unittest.TestCase):
    def testSearchMatrix(self):
        s = Solution()
        self.assertEqual(s.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3), True)
        self.assertEqual(s.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13), False)


if __name__ == '__main__':
    unittest.main()