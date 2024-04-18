from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.heap = []
        for num in nums:
            self._handle(num)

    def add(self, val: int) -> int:
        self.nums.append(val)
        self._handle(val)
        return self.heap[0]

    def _handle(self, num):
        if not self.heap or len(self.heap) < self.k or num > self.heap[0]:
            heapq.heappush(self.heap, num)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

class Solution:
    pass


import unittest

class TestSolution(unittest.TestCase):
    def testKthLargest(self):
        k = KthLargest(k=3, nums=[4,5,8,2])
        self.assertEqual(k.add(val=3), 4)
        self.assertEqual(k.add(val=5), 5)
        self.assertEqual(k.add(val=10), 5)
        self.assertEqual(k.add(val=9), 8)
        self.assertEqual(k.add(val=4), 8)

    def testKthLargest1(self):
        k = KthLargest(k=1, nums=[])
        self.assertEqual(k.add(val=-3), -3)
        self.assertEqual(k.add(val=-2), -2)
        self.assertEqual(k.add(val=-4), -2)
        self.assertEqual(k.add(val=0), 0)
        self.assertEqual(k.add(val=4), 4)

    def testKthLargest2(self):
        k = KthLargest(k=2, nums=[0])
        self.assertEqual(k.add(val=-1), -1)
        self.assertEqual(k.add(val=1), 0)
        self.assertEqual(k.add(val=-2), 0)
        self.assertEqual(k.add(val=-4), 0)
        self.assertEqual(k.add(val=3), 1)



if __name__ == '__main__':
    unittest.main()