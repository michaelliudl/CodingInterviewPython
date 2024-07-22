from typing import List, Deque, DefaultDict

class Solution:

    # Input conditions are ordered and form edges of a graph
    # Use BFS or DFS to build topological sorted elements for both row and column conditions
    # Each element in the topological sorted array has its row/column index in the result array
    # Input is invalid if either topological sorted row or column conditions have cycle
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        def dfs(elem, graph, visited, elementsOnPath, topo):
            if elem in elementsOnPath:  # Cycle detected
                return False
            if elem in visited:
                return True
            visited.add(elem)
            elementsOnPath.add(elem)
            for neighbor in graph[elem]:
                if not dfs(neighbor, graph, visited, elementsOnPath, topo):
                    return False
            topo.append(elem)
            elementsOnPath.remove(elem)
            return True

        def topoSortDFS(edges):
            graph = DefaultDict(list)
            for u, v in edges:
                graph[u].append(v)
            visited, elemsOnPath = set(), set()    # `elemsOnPath` contains visited elements on current paths and is used to detect cycle
            topo = []   # Topological sorted all elements in edges
            for elem in range(1, k + 1):
                if not dfs(elem, graph, visited, elemsOnPath, topo):
                    return []
            return topo[::-1]   # DFS adds elements without neighbors first, so reverse it
        
        def topoSortBFS(edges):
            graph = [[] for _ in range(k + 1)]
            inDegrees = [0] * (k + 1)
            for u, v in edges:
                graph[u].append(v)
                inDegrees[v] += 1
            
            res = []
            queue = Deque()
            for elem in range(1, k + 1):
                if inDegrees[elem] == 0:    # Start with nodes without incoming edges
                    queue.append(elem)
            while queue:
                elem = queue.popleft()
                res.append(elem)
                for neighbor in graph[elem]:
                    inDegrees[neighbor] -= 1    # Decrement neighbor's in-degree
                    if inDegrees[neighbor] == 0:    # `neighbor` will never be enqueued if there is cycle
                        queue.append(neighbor)
            return res if len(res) == k else []

        def topoSort(edges):
            # res = topoSortDFS(edges)
            res = topoSortBFS(edges)
            return res

        rowTopo = topoSort(rowConditions)
        if not rowTopo:
            return []
        colTopo = topoSort(colConditions)
        if not colTopo:
            return []
        elemsRow = {elem: index for index, elem in enumerate(rowTopo)}  # Convert to elements to row/column index map
        elemsCol = {elem: index for index, elem in enumerate(colTopo)}
        res = [[0] * k for _ in range(k)]
        for elem in range(1, k + 1):
            i, j = elemsRow[elem], elemsCol[elem]
            res[i][j] = elem
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testBuildMatrix(self):
        s = Solution()
        self.assertEqual(s.buildMatrix(k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]), 
                         [[3,0,0],[0,0,1],[0,2,0]])
        self.assertEqual(s.buildMatrix(k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions = [[2,1]]), 
                         [])


if __name__ == '__main__':
    unittest.main()