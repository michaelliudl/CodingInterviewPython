from typing import List
import heapq

class Solution:
    # Similar to 1383
    # Create array (wage / quality, quality) and sort by wage / quality ratio in ascending order.
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        if len(quality) != len(wage): return -1
        workers,n = [],len(quality)
        for i in range(n):
            workers.append((wage[i] / quality[i], quality[i]))
        workers.sort()
        heap = []
        cost,totalQuality = float('inf'),0
        for ratio, curQuality in workers:
            heapq.heappush(heap, -curQuality)       # Max heap for qualities
            totalQuality += curQuality
            if len(heap) == k:                      # Exactly k
                cost = min(cost, totalQuality * ratio)
                maxQuality = -heapq.heappop(heap)
                totalQuality -= maxQuality
        return cost



import unittest

class TestSolution(unittest.TestCase):
    def testMincostToHireWorkers(self):
        s = Solution()
        self.assertEqual(s.mincostToHireWorkers(quality = [10,20,5], wage = [70,50,30], k = 2), 105.0)
        self.assertTrue(s.mincostToHireWorkers(quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3) - 30.66667 < 10 ** -5)
        


if __name__ == '__main__':
    unittest.main()