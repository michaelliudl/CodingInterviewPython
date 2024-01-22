from typing import List
from typing import Deque


class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        
        
        



import unittest

class TestSolution(unittest.TestCase):
    def testTrap(self):
        s = Solution()
        self.assertEqual(s.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]), 6)
        self.assertEqual(s.trap(height = [4,2,0,3,2,5]), 9)



if __name__ == '__main__':
    unittest.main()