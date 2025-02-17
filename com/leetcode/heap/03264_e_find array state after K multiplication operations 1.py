from typing import List
import heapq, math

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(num, index) for index, num in enumerate(nums)]
        heapq.heapify(heap)
        for _ in range(k):
            num, index = heapq.heappop(heap)
            heapq.heappush(heap, (num * multiplier, index))
        heap.sort(key=lambda elem:elem[1])
        return [num for num, _ in heap]



import unittest

class TestSolution(unittest.TestCase):
    def testLastStoneWeight(self):
        s = Solution()
        self.assertEqual(s.lastStoneWeight(stones = [2,7,4,1,8,1]), 1)
        self.assertEqual(s.lastStoneWeight(stones=[1]), 1)



if __name__ == '__main__':
    unittest.main()