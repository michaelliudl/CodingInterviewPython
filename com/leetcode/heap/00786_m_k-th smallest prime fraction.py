from typing import List, DefaultDict
import heapq
from sortedcontainers import SortedList

class Solution:

    # O((n**2)log(n)), O(nlog(max)) solution for followup is involved
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        n = len(arr)
        for i in range(n - 1):
            for j in range(i + 1, n):
                frac = arr[i] / arr[j]
                heapq.heappush(heap, (-frac, arr[i], arr[j]))
                while len(heap) > k:
                    heapq.heappop(heap)
        return [heap[0][1], heap[0][2]]


import unittest

class TestSolution(unittest.TestCase):
    def testMostFrequentIDs(self):
        s = Solution()
        self.assertEqual(s.mostFrequentIDs(nums = [2,3,2,1], freq = [3,2,-3,1]), [3,3,2,2])
        self.assertEqual(s.mostFrequentIDs(nums = [5,5,3], freq = [2,-2,1]), [2,0,1])
        


if __name__ == '__main__':
    unittest.main()