from typing import List

'''
There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.
'''

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        if not heights:
            return heights
        result = [0]
        for i in range(1, len(heights)):
            while result and heights[i] >= heights[result[-1]]:
                result.pop()
            result.append(i)
        return result


import unittest

class TestSolution(unittest.TestCase):
    def testSimplifyPath(self):
        s = Solution()
        self.assertEqual(s.simplifyPath("/home/"), "/home")
        self.assertEqual(s.simplifyPath("/../"), "/")
        self.assertEqual(s.simplifyPath("/home//foo/"), "/home/foo")



if __name__ == '__main__':
    unittest.main()