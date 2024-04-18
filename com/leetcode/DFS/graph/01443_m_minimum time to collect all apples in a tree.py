from typing import List

class Solution:

    # Actually graph since test case has edges from leaf to parent
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        def dfs(node):
            if node not in graph or not graph[node]:
                return (hasApple[node], 0)
            visited.add(node)
            childrenTime = 0
            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    hasApp, childTime = dfs(child)
                    if hasApp:
                        childrenTime += childTime + 2
            if childrenTime > 0:
                return (True, childrenTime)
            else:
                return (hasApple[node], 0)
        
        def buildGraph():
            graph = {}
            for start, end in edges:
                if start not in graph:
                    graph[start] = set()
                graph[start].add(end)
                if end not in graph:
                    graph[end] = set()
                graph[end].add(start)
            return graph

        if not edges or all(not has for has in hasApple):
            return 0
        graph = buildGraph()
        visited = set()
        _, time = dfs(node = 0)
        return time
        

import unittest

class TestSolution(unittest.TestCase):
    def testMinTime(self):
        s = Solution()
        self.assertEqual(s.minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,True,True,False]), 8)
        self.assertEqual(s.minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,False,True,False]), 6)
        self.assertEqual(s.minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,False,False,False,False,False]), 0)
        self.assertEqual(s.minTime(n = 4, edges = [[0,2],[0,3],[1,2]], hasApple = [False,True,False,False]), 4)


if __name__ == '__main__':
    unittest.main()