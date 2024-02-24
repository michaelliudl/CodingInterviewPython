from typing import List
import heapq

class Solution:

    # Dijkstra's algorithm, with distance cache
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {}
        for start,end,price in flights:
            if start not in graph:
                graph[start] = []
            graph[start].append((end,price))
        # Cache distance from each node, up to k+1 steps away
        distCache = [[float('inf') for _ in range(k+2)] for _ in range(n)]
        distCache[src][0] = 0
        heap = [(0,src,0)]  # Price, Stops, Node. Lowest price as shorted path
        while heap:
            dist,cur,stops = heapq.heappop(heap)
            if cur == dst:
                return dist
            if stops > k or cur not in graph:
                continue
            for next,weight in graph[cur]:
                if dist + weight < distCache[next][stops+1]:
                    distCache[next][stops+1] = dist + weight
                    heapq.heappush(heap, (dist+weight, next, stops+1))
        return -1

    # Brute DFS
    def findCheapestPriceBrute(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        def buildGraph():
            for start,end,price in flights:
                if start not in graph:
                    graph[start] = []
                graph[start].append((end,price))

        def dfs(start, stops, totalPrice):
            nonlocal ans
            if start == dst and stops <= k+1:
                ans = min(ans, totalPrice)
                return
            if stops == k+1:
                return
            if start in graph:
                for next,price in graph[start]:
                    dfs(next, stops+1, totalPrice+price)

        graph = {}
        buildGraph()
        ans = float('inf')
        dfs(start=src, stops=0, totalPrice=0)
        return ans if ans < float('inf') else -1


import unittest

class TestSolution(unittest.TestCase):
    def testFindCheapestPrice(self):
        s = Solution()
        self.assertEqual(s.findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1), 700)
        self.assertEqual(s.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1), 200)
        self.assertEqual(s.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0), 500)


if __name__ == '__main__':
    unittest.main()