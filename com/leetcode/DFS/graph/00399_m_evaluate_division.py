from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        def buildGraph():
            for i in range(n):
                var1, var2 = equations[i]
                value = values[i]
                if var1 not in graph:
                    graph[var1] = set()
                if var2 not in graph:
                    graph[var2] = set()
                graph[var1].add((var2, value))
                graph[var2].add((var1, 1 / value))
        
        def dfs(start, end, index, value, visited):
            if start == end:
                ans[index] = value
                return
            visited.add(start)
            for next, nextValue in graph[start]:
                if next not in visited:
                    dfs(next, end, index, value * nextValue, visited)

        if not equations or not values or not queries or len(equations) != len(values):
            return []
        n = len(equations)
        graph = {}
        buildGraph()
        ans = [-1] * len(queries)
        for i in range(len(queries)):
            start, end = queries[i][0], queries[i][1]
            if start not in graph or end not in graph:
                continue
            visited = set()
            dfs(start, end, index = i, value = 1, visited = visited)
        return ans

import unittest

class TestSolution(unittest.TestCase):
    def testCalcEquation(self):
        s = Solution()
        self.assertEqual(s.calcEquation(equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]), 
                         [6.00000,0.50000,-1.00000,1.00000,-1.00000])
        self.assertEqual(s.calcEquation(equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]), 
                         [3.75000,0.40000,5.00000,0.20000])
        self.assertEqual(s.calcEquation(equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]), 
                         [0.50000,2.00000,-1.00000,-1.00000])


if __name__ == '__main__':
    unittest.main()