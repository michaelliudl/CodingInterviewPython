from typing import List
from typing import Deque


class Solution:

    # Monotonic stack
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        def largestRectangleInHistogram(histogram):
            ret = 0
            histogram = [0] + histogram + [0]
            stack = [0]
            for i in range(1, len(histogram)):
                curHist = histogram[i]
                while stack and curHist < histogram[stack[-1]]:
                    midHist = histogram[stack.pop()]
                    leftIndex = stack[-1]
                    rectangle = midHist * (i - leftIndex - 1)
                    ret = max(ret, rectangle)
                stack.append(i)
            return ret

        if not matrix:
            return 0
        n = len(matrix[0])
        histogram = [0] * n
        result = 0
        for row in matrix:
            for i in range(n):      # Create histogram for each row, column value sums for continuous `1`s, otherwise 0
                if row[i] == '1':
                    histogram[i] += 1
                else:
                    histogram[i] = 0
            # result = max(result, largestRectangleInHistogram(histogram))
            # Logic for # 84 below or in separate function
            curHist = [0] + histogram + [0]
            stack = [0]
            for i in range(1, len(curHist)):
                while curHist[i] < curHist[stack[-1]]:
                    height = curHist[stack.pop()]
                    width = i - stack[-1] - 1
                    result = max(result, height * width)
                stack.append(i)
        return result
        
        



import unittest

class TestSolution(unittest.TestCase):
    def testMaximalRectangle(self):
        s = Solution()
        self.assertEqual(s.maximalRectangle(matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]), 6)
        self.assertEqual(s.maximalRectangle(matrix = [["0","1"],["1","0"]]), 1)
        self.assertEqual(s.maximalRectangle(matrix = [["0"]]), 0)
        self.assertEqual(s.maximalRectangle(matrix = [["1"]]), 1)



if __name__ == '__main__':
    unittest.main()