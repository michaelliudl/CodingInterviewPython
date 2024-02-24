from typing import List,Deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:

    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n<=1: return n
        trustOthers,trustedBy = {},{}
        for a,b in trust:
            if a not in trustOthers:
                trustOthers[a] = []
            if b not in trustedBy:
                trustedBy[b] = []
            trustOthers[a].append(b)
            trustedBy[b].append(a)
        for i in range(1,n+1):
            if i not in trustOthers or not trustOthers[i]:
                if i in trustedBy and len(trustedBy[i]) == n-1:
                    return i
        return -1
        

import unittest

class TestSolution(unittest.TestCase):
    def testCanFinish(self):
        s = Solution()
        self.assertEqual(s.canFinish(numCourses = 2, prerequisites = [[1,0]]), True)
        self.assertEqual(s.canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]]), False)
        


if __name__ == '__main__':
    unittest.main()