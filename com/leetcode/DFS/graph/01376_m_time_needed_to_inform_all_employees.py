from typing import List,Deque

class Solution:

    # DFS to find time to inform each one and find max
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        def buildGraph():
            for i in range(n):
                if i not in graph:
                    graph[i] = set()
                if manager[i] not in graph:
                    graph[manager[i]] = set()
                graph[manager[i]].add(i)
        
        def dfs(empId, time):
            recvTime[empId] = time
            if informTime[empId] == 0:
                return
            for reportId in graph[empId]:
                if recvTime[reportId] == 0:
                    dfs(reportId, time + informTime[empId])

        if headID < 0 or headID >= n or len(manager) != n or len(informTime) != n:
            return -1
        graph = {}
        buildGraph()
        recvTime = [0] * n
        dfs(empId = headID, time = 0)
        ans = max(recvTime)
        return ans

import unittest

class TestSolution(unittest.TestCase):
    def testNumOfMinutes(self):
        s = Solution()
        self.assertEqual(s.numOfMinutes(n = 11, headID = 4, manager = [5,9,6,10,-1,8,9,1,9,3,4], informTime = [0,213,0,253,686,170,975,0,261,309,337]), 2560)
        self.assertEqual(s.numOfMinutes(n = 15, headID = 0, manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]), 3)
        self.assertEqual(s.numOfMinutes(n = 1, headID = 0, manager = [-1], informTime = [0]), 0)
        self.assertEqual(s.numOfMinutes(n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]), 1)


if __name__ == '__main__':
    unittest.main()