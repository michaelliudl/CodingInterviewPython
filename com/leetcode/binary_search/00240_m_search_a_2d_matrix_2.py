from typing import List

class Solution:

    # Indirect binary search.
    # Start from top-right or bottom left corner.
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def fromTopRight():
            row,col = 0,n-1     # From top-right
            while row < m and col >= 0:
                if matrix[row][col] == target:
                    return True
                elif matrix[row][col] > target:
                    col -= 1
                else:
                    row += 1
            return False

        def fromBottomLeft():
            row,col = m-1,0
            while row>=0 and col<n:
                if matrix[row][col] == target:
                    return True
                elif matrix[row][col] > target:
                    row -= 1
                else:
                    col += 1
            return False

        if not matrix: return False
        m,n = len(matrix),len(matrix[0])
        # return fromTopRight()
        return fromBottomLeft()
            

import unittest

class TestSolution(unittest.TestCase):
    def testTwoSum(self):
        s = Solution()
        self.assertEqual(s.twoSum([2,7,11,15],9), [0,1])
        self.assertEqual(s.twoSum([3,2,4],6), [1,2])
        self.assertEqual(s.twoSum([3,3],6), [0,1])


if __name__ == '__main__':
    unittest.main()