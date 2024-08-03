from typing import List, Deque, DefaultDict

class Solution:

    # BFS and cache visit time to nodes
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = DefaultDict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        queue = Deque()
        queue.append(1)
        curTime = 0
        destVisited = False
        cache = DefaultDict(list)   # Cache visit time to nodes
        while queue:
            curLen = len(queue)
            for _ in range(curLen):
                cur = queue.popleft()
                if cur == n:
                    if destVisited:
                        return curTime
                    destVisited = True
                for neighbor in graph[cur]:
                    neighborTime = cache[neighbor]
                    if not neighborTime or (len(neighborTime) == 1 and curTime != neighborTime[0]):
                        queue.append(neighbor)
                        neighborTime.append(curTime)

            if (curTime // change) % 2 == 1:
                curTime += (change - (curTime % change))
            curTime += time

        

import unittest

class TestSolution(unittest.TestCase):
    def testSecondMinimum(self):
        s = Solution()
        self.assertEqual(s.secondMinimum(n = 5, edges = [[1,2],[1,3],[1,4],[3,4],[4,5]], time = 3, change = 5), 13)
        self.assertEqual(s.secondMinimum(n = 2, edges = [[1,2]], time = 3, change = 2), 11)


if __name__ == '__main__':
    unittest.main()