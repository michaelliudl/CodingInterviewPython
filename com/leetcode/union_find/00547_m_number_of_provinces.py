from typing import List,Deque

class Solution:

    # TODO Union Find

    # BFS
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def buildGraph():
            for i in range(n):
                for j in range(i + 1, n):
                    if isConnected[i][j] == 1:
                        if i not in graph:
                            graph[i] = set()
                        if j not in graph:
                            graph[j] = set()
                        graph[i].add(j)
                        graph[j].add(i)
        
        def bfs(start):
            queue = Deque()
            queue.append(start)
            while queue:
                node = queue.popleft()
                used.add(node)
                if node in graph:
                    for neighbor in graph[node]:
                        if neighbor not in used:
                            used.add(neighbor)
                            queue.append(neighbor)

        if not isConnected:
            return 0
        n = len(isConnected)
        graph = {}
        buildGraph()
        used = set()
        ans = 0
        for i in range(n):
            if i in used:
                continue
            ans += 1
            used.add(i)
            if i in graph:
                bfs(i)
        return ans


import unittest

class TestSolution(unittest.TestCase):
    def testFindCircleNum(self):
        s = Solution()
        self.assertEqual(s.findCircleNum(isConnected = [[1,1,0],[1,1,0],[0,0,1]]), 2)
        self.assertEqual(s.findCircleNum(isConnected = [[1,0,0],[0,1,0],[0,0,1]]), 3)
        self.assertEqual(s.findCircleNum(isConnected = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]), 1)


if __name__ == '__main__':
    unittest.main()