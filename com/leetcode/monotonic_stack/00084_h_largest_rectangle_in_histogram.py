from typing import List
from typing import Deque


class Solution:

    # Monotonic stack
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        heights = [0] + heights + [0]   # Add dummy elements to front for getting start index, and to back for all ascending case
        stack = [0]             # Stack holds index
        result = 0
        for i in range(1, len(heights)):
            curHeight = heights[i]
            while stack and curHeight < heights[stack[-1]]:
                midIndex = stack.pop()
                midHeight = heights[midIndex]
                leftIndex = stack[-1]
                area = midHeight * (i - leftIndex - 1)
                result = max(result, area)
            stack.append(i)
        return result

    # Two pointer to find index of first smaller element to each index. First and last element is initialized -1 and n
    def largestRectangleAreaTwoPointer(self, heights: List[int]) -> int:
        if not heights:
            return 0
        n=len(heights)
        smallLeftIdx=[-1]*n
        for i in range(1,n):
            temp = i-1
            while temp >=0 and heights[temp] >= heights[i]:
                temp = smallLeftIdx[temp]
            smallLeftIdx[i] = temp
        smallRightIdx=[n]*n
        for i in range(n-2,-1,-1):
            temp = i+1
            while temp<n and heights[temp] >= heights[i]:
                temp = smallRightIdx[temp]
            smallRightIdx[i] = temp
        largest=0
        for i in range(n):
            area = heights[i] * (smallRightIdx[i] - smallLeftIdx[i] - 1)
            largest=max(largest, area)
        return largest
        
        



import unittest

class TestSolution(unittest.TestCase):
    def testLargestRectangleArea(self):
        s = Solution()
        self.assertEqual(s.largestRectangleArea(heights = [2,1,5,6,2,3]), 10)
        self.assertEqual(s.largestRectangleArea(heights = [2,4]), 4)



if __name__ == '__main__':
    unittest.main()