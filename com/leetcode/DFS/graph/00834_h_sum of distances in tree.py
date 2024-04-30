from typing import List,Deque,DefaultDict

class Solution:

    # DFS from root 0, find sub-tree size of each node, also find total distance from root to all other nodes
    # Re-root the tree to each other node, total_distance[node] = total_distance[parent] - subtree_size[node] + (n - subtree_size[node])
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:

        def dfsSubtreeSize(node, parent = None):
            for child in graph[node]:
                if child == parent:
                    continue
                dfsSubtreeSize(child, node)
                subtreeSizes[node] += subtreeSizes[child]
                totalDists[node] += (totalDists[child] + subtreeSizes[child])
        
        def dfsTotalDist(node, parent = None):
            for child in graph[node]:
                if child == parent:
                    continue
                totalDists[child] = totalDists[node] - subtreeSizes[child] + (n - subtreeSizes[child])
                dfsTotalDist(child, node)

        graph = DefaultDict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        subtreeSizes = [1] * n      # Including root
        totalDists = [0] * n
        dfsSubtreeSize(node = 0)
        dfsTotalDist(node = 0)
        return totalDists

    # Brute, BFS from each node, O(N**2)
    def sumOfDistancesInTreeBrute(self, n: int, edges: List[List[int]]) -> List[int]:

        def bfs(startNode):
            queue = Deque()
            queue.append((startNode, 0))     # Also enqueue distance from starting node
            visited = set()
            visited.add(startNode)
            res = 0
            dist = 0
            while queue:
                node, dist = queue.popleft()
                res += dist
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, dist + 1))
                        visited.add(neighbor)
            return res

        graph = DefaultDict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        return [bfs(i) for i in range(n)]

import unittest

class TestSolution(unittest.TestCase):
    def testSumOfDistancesInTree(self):
        s = Solution()
        self.assertEqual(s.sumOfDistancesInTree(n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]), [8,12,6,10,10,10])
        self.assertEqual(s.sumOfDistancesInTree(n = 1, edges = []), [0])
        self.assertEqual(s.sumOfDistancesInTree(n = 2, edges = [[1,0]]), [1,1])


if __name__ == '__main__':
    unittest.main()