from typing import List
import heapq

class Solution:

    # Binary search
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        # Count from bottom-left
        def countLessOrEqual(target):
            count = 0
            row,col = m-1,0
            while row>=0 and col<n:
                if matrix[row][col] <= target:
                    count += row + 1            # All values in this column above `row` are less than `target`
                    col += 1
                else:
                    row -= 1
            return count

        if not matrix or k < 0: return 0
        m,n = len(matrix),len(matrix[0])
        low,high = matrix[0][0], matrix[m-1][n-1]
        while low < high:
            mid = low + (high-low) // 2
            # Find number of elements that are less than or equal to `mid`
            count = countLessOrEqual(mid)
            if count >= k:
                high = mid
            else:
                low = mid + 1
        return low

    # Heap
    def kthSmallestHeap(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or k < 0: return 0
        heap = []
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if len(heap) < k:
                    heapq.heappush(heap, -matrix[i][j])
                elif matrix[i][j] < -heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, -matrix[i][j])
        return -heap[0]


import unittest

class TestSolution(unittest.TestCase):
    def testKClosest(self):
        s = Solution()
        self.assertEqual(sorted(s.kClosest(points = [[1,3],[-2,2]], k = 1)), sorted([[-2,2]]))
        self.assertEqual(sorted(s.kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2)), sorted([[3,3],[-2,4]]))



if __name__ == '__main__':
    unittest.main()