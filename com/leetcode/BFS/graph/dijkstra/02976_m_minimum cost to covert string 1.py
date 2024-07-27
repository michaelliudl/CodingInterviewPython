from typing import List, DefaultDict
import heapq, math

class Solution:

    # Dijkstra to find lowest weight paths
    def minimumCostDijkstra(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        def dijkstra(src):      # Dijkstra to find reachable dest from src and min distance
            heap = [(0, src)]
            distMap = {}
            while heap:
                dist, cur = heapq.heappop(heap)
                if cur not in distMap or dist < distMap[cur]:
                    distMap[cur] = dist
                    for neighbor, neighborDist in graph[cur]:
                        if neighbor not in distMap:
                            heapq.heappush(heap, ((dist + neighborDist), neighbor))
            return distMap

        graph = DefaultDict(list)
        for src, dest, dist in zip(original, changed, cost):
            graph[src].append((dest, dist))
        distMap = {char: dijkstra(char) for char in set(source)}    # Calculate distMap for each unique char in source
        res = 0
        for src, dest in zip(source, target):
            if dest not in distMap[src]:    # Unreachable
                return -1
            res += distMap[src][dest]
        return res

    # Floyd-Warshall to find shortest distance to change character from source to dest
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        fwDist = [[math.inf] * 26 for _ in range(26)]   # Lower case only
        for src, dest, dist in zip(original, changed, cost):
            i = ord(src) - ord('a')
            j = ord(dest) - ord('a')
            fwDist[i][j] = min(fwDist[i][j], dist)

        for k in range(26):
            for i in range(26):
                if fwDist[i][k] < math.inf:
                    for j in range(26):
                        if fwDist[k][j] < math.inf:
                            fwDist[i][j] = min(fwDist[i][j], (fwDist[i][k] + fwDist[k][j]))
        res = 0
        for src, dest in zip(source, target):
            if src != dest:
                i = ord(src) - ord('a')
                j = ord(dest) - ord('a')
                if fwDist[i][j] == math.inf:
                    return -1
                res += fwDist[i][j]
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testMinimumCost(self):
        s = Solution()
        self.assertEqual(s.minimumCost(source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]), 28)
        self.assertEqual(s.minimumCost(source = "aaaa", target = "bbbb", original = ["a","c"], changed = ["c","b"], cost = [1,2]), 12)
        self.assertEqual(s.minimumCost(source = "abcd", target = "abce", original = ["a"], changed = ["e"], cost = [10000]), -1)


if __name__ == '__main__':
    unittest.main()