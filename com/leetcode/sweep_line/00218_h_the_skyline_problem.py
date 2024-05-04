from typing import List
import heapq, math
from sortedcontainers import SortedList

class Solution:

    # Separate left and right sides of buildings and use heap or sorted list to find max height on the boundaries of each building
    # Sort left side asc and heights desc, use 0 height to label right side
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        sides = []
        for left, right, height in buildings:
            sides.append([left, -height, right])    # Take -height to sort it desc, when left is same, largest height takes precedence
            sides.append([right, 0, 0])             # Add each right side to process removing the building from collection
        sides.sort()        # Sort all left and right sides together
        res = []
        heap = [(0, math.inf)]      # Start with 0 height and inf location on x axis
        for loc, height, right in sides:
            if height < 0:          # Building's left side
                heapq.heappush(heap, (height, right))
            while heap[0][1] <= loc:    # Horizontally moved out of highest building in heap
                heapq.heappop(heap)
            if not res or res[-1][1] != -heap[0][0]:     # First building or this one is not same height as last one
                res.append([loc, -heap[0][0]])
        return res


import unittest

class TestSolution(unittest.TestCase):
    def testMinAddToMakeValid(self):
        s = Solution()
        self.assertEqual(s.minAddToMakeValid("())"), 1)
        self.assertEqual(s.minAddToMakeValid("((("), 3)


if __name__ == '__main__':
    unittest.main()