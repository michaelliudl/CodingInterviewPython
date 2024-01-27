from typing import List
from typing import Deque


class Solution:

    # Monotonic stack
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        pass
        
        



import unittest

class TestSolution(unittest.TestCase):
    def testLargestRectangleArea(self):
        s = Solution()
        self.assertEqual(s.largestRectangleArea(heights = [2,1,5,6,2,3]), 10)
        self.assertEqual(s.largestRectangleArea(heights = [2,4]), 4)



if __name__ == '__main__':
    unittest.main()