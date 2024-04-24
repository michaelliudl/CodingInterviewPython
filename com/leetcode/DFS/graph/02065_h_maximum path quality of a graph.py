from typing import List, DefaultDict

class Solution:

    # DFS all possibilities
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:

        def dfs(node, quality, time):
            nonlocal ret
            if node == 0:
                ret = max(ret, quality)
            for neighbor, neighborTime in graph[node]:
                if time + neighborTime <= maxTime:
                    newQuality = quality + (values[neighbor] if visitCount[neighbor] == 0 else 0)
                    visitCount[neighbor] += 1
                    dfs(neighbor, newQuality, time + neighborTime)
                    visitCount[neighbor] -= 1

        if not values:
            return 0
        n = len(values)
        graph = DefaultDict(list)
        for u, v, time in edges:
            graph[u].append((v, time))
            graph[v].append((u, time))
        ret = 0
        visitCount = DefaultDict(int)
        visitCount[0] = 1
        dfs(node = 0, quality = values[0], time = 0)
        return ret

import unittest

class TestSolution(unittest.TestCase):
    def testMaximalPathQuality(self):
        s = Solution()
        self.assertEqual(s.maximalPathQuality(values = [95], edges = [], maxTime = 83), 95)
        self.assertEqual(s.maximalPathQuality(values = [0,32,10,43], edges = [[0,1,10],[1,2,15],[0,3,10]], maxTime = 49), 75)
        self.assertEqual(s.maximalPathQuality(values = [5,10,15,20], edges = [[0,1,10],[1,2,10],[0,3,10]], maxTime = 30), 25)
        self.assertEqual(s.maximalPathQuality(values = [1,2,3,4], edges = [[0,1,10],[1,2,11],[2,3,12],[1,3,13]], maxTime = 50), 7)

if __name__ == '__main__':
    unittest.main()