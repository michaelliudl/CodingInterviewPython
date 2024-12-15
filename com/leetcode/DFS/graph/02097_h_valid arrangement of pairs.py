from typing import List, DefaultDict

class Solution:

    # Calculate Euler Circuit of the graph
    def validArrangement(self, pairs: list[list[int]]) -> list[list[int]]:

        def findStart():
            for node, _ in graph.items():
                if outDegree[node] - inDegree[node] == 1:
                    return node
            return pairs[0][0]  # Default start from first node

        def eulerCircuit(node):
            neighbors = graph[node]
            while neighbors:
                neighbor = neighbors.pop()
                eulerCircuit(neighbor)
                res.append([node, neighbor])

        graph = DefaultDict(list)
        inDegree = DefaultDict(int)
        outDegree = DefaultDict(int)
        for start, end in pairs:
            graph[start].append(end)
            outDegree[start] += 1
            inDegree[end] += 1
        start = findStart()
        res = []
        eulerCircuit(node=start)
        res.reverse()
        return res


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