from typing import List,Deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pass
        

import unittest

class TestSolution(unittest.TestCase):
    def testNumIslands(self):
        s = Solution()
        self.assertEqual(s.numIslands(grid = [
                        ["1","1","1","1","0"],
                        ["1","1","0","1","0"],
                        ["1","1","0","0","0"],
                        ["0","0","0","0","0"]
                        ]), 1)
        self.assertEqual(s.numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
                        ]), 3)
        


if __name__ == '__main__':
    unittest.main()