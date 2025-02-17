from typing import List, DefaultDict

class Solution:

    # The result tree's diameter is the max of (the diameters of the original trees, 1 + the sum of the roundup half of the diameters of the original trees).
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        
        # Similar to 1522, diameter of N-ary tree
        def getDiameter(edges):
            graph = [[] for _ in range(len(edges) + 1)]
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)

            getMaxDepth(graph, node=0, parent=-1)
        
        def getMaxDepth(graph, node, parent):
            nonlocal diameter

            maxSubDepth1 = maxSubDepth2 = 0
            for neightbor in graph[node]:
                if neightbor == parent:
                    continue
                maxSubDepth = getMaxDepth(graph, neightbor, node)
                if maxSubDepth > maxSubDepth1:
                    maxSubDepth2 = maxSubDepth1
                    maxSubDepth1 = maxSubDepth
                elif maxSubDepth > maxSubDepth2:
                    maxSubDepth2 = maxSubDepth
            diameter = max(diameter, maxSubDepth1 + maxSubDepth2)
            return 1 + maxSubDepth1
            
        diameter = 0
        getDiameter(edges1)
        diameter1 = diameter
        # Reset diameter for the second tree
        diameter = 0
        getDiameter(edges2)
        diameter2 = diameter
        # Calculate the combined diameter
        combinedDiameter = 1 + (diameter1 + 1) // 2 + (diameter2 + 1) // 2
        return max(diameter1, diameter2, combinedDiameter)

import unittest

class TestSolution(unittest.TestCase):
    def testFindItinerary(self):
        s = Solution()
        self.assertEqual(s.canCross(stones = [0,1,3,5,6,8,12,17]), True)
        self.assertEqual(s.canCross(stones = [0,1,2,3,4,8,9,11]), False)

if __name__ == '__main__':
    unittest.main()