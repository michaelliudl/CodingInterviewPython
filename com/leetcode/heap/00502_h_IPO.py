from typing import List
import heapq

class Solution:

    # Use min heap to find projects' `capital` that is less than `w`
    # Use max heap to get largest `profit` to get from current `w`
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minHeap = list(zip(capital, profits))
        heapq.heapify(minHeap)
        maxHeap = []
        while k > 0:
            while minHeap and minHeap[0][0] <= w:
                cap, prof = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, (-prof, cap))
            if not maxHeap:
                break
            w -= heapq.heappop(maxHeap)[0]
            k -= 1
        return w


import unittest

class TestSolution(unittest.TestCase):
    def testFindMaximizedCapital(self):
        s = Solution()
        self.assertEqual(s.findMaximizedCapital(k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]), 4)
        self.assertEqual(s.findMaximizedCapital(k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]), 6)


if __name__ == '__main__':
    unittest.main()