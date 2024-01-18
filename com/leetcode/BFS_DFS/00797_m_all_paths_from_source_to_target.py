from typing import List,Deque

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        def dfs(graph, node, r, path):
            if node==len(graph)-1:
                r.append(path[:])
                return
            for v in graph[node]:
                path.append(v)
                dfs(graph, v, r, path)
                path.pop()

        if not graph:
            return [[]]
        r=[]
        dfs(graph, node=0, r=r, path=[0])
        return r
        

import unittest

class TestSolution(unittest.TestCase):
    def testAllPathsSourceTarget(self):
        s = Solution()
        self.assertEqual(s.allPathsSourceTarget(graph = [[1,2],[3],[3],[]]), [[0,1,3],[0,2,3]])
        self.assertEqual(s.allPathsSourceTarget(graph = [[4,3,1],[3,2,4],[3],[4],[]]), [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]])
        


if __name__ == '__main__':
    unittest.main()