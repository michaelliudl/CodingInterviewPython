from typing import List
import heapq, math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-gift for gift in gifts]
        heapq.heapify(heap)
        for _ in range(k):
            gift = -heapq.heappop(heap)
            heapq.heappush(heap, -int(math.sqrt(gift)))
        return -sum(heap)



import unittest

class TestSolution(unittest.TestCase):
    def testLastStoneWeight(self):
        s = Solution()
        self.assertEqual(s.lastStoneWeight(stones = [2,7,4,1,8,1]), 1)
        self.assertEqual(s.lastStoneWeight(stones=[1]), 1)



if __name__ == '__main__':
    unittest.main()