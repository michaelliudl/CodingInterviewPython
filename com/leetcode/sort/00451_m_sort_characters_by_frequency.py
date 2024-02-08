from typing import List
import heapq
import random

class Solution:
    def frequencySort(self, s: str) -> str:
        if not s: return s
        freq={}
        for c in s:
            if c in freq: freq[c]+=1
            else: freq[c]=1
        heap=[]
        for k,v in freq.items():
            heapq.heappush(heap, (-v,k))
        ans=[]
        while heap:
            count,c=heapq.heappop(heap)
            for _ in range(-count):
                ans.append(c)
        return ''.join(ans)


import unittest

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def testFindKthLargest(self):
        self.assertEqual(self.s.findKthLargestQuickSelect([3,2,1,5,6,4],2), 5)
        self.assertEqual(self.s.findKthLargestQuickSelect([3,2,3,1,2,4,5,5,6],4), 4)
        # self.s.partition([3,2,3,1,2,4,5,5,6], 0, 8)


if __name__ == '__main__':
    unittest.main()