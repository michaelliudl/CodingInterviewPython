from typing import List
import heapq

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        if len(speed) != n or len(efficiency) != n: return 0
        MOD = 10 ** 9 + 7
        combinations = []
        for i in range(n):
            combinations.append((efficiency[i], speed[i]))
        combinations.sort(reverse=True)
        ans,totalSpeed = 0,0
        heap = []
        for curEffi, curSpeed in combinations:
            heapq.heappush(heap, curSpeed)
            totalSpeed += curSpeed
            if len(heap) > k:
                leastSpeed = heapq.heappop(heap)
                totalSpeed -= leastSpeed
            ans = max(ans, (totalSpeed * curEffi))
        return ans % MOD



import unittest

class TestSolution(unittest.TestCase):
    def testMaxPerformance(self):
        s = Solution()
        self.assertEqual(s.maxPerformance(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4), 72)
        self.assertEqual(s.maxPerformance(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2), 60)
        self.assertEqual(s.maxPerformance(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3), 68)
        


if __name__ == '__main__':
    unittest.main()