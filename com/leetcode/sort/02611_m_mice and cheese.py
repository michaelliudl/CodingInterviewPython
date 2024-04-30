from typing import List
from typing import Deque
import heapq

class Solution:

    # Use min heap to track largest diff between reward1 and reward2
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        heap = []
        for i in range(n):
            diff = reward1[i] - reward2[i]
            if k > 0 and len(heap) == k and heap[0] < diff:
                heapq.heappop(heap)
            if len(heap) < k:
                heapq.heappush(heap, diff)
        return sum(reward2) + sum(heap)     # Since heap contains k largest (reward1 - reward2)

import unittest

class TestSolution(unittest.TestCase):
    def testMiceAndCheese(self):
        s = Solution()
        self.assertEqual(s.miceAndCheese(reward1 = [1,1,3,4], reward2 = [4,4,1,1], k = 2), 15)
        self.assertEqual(s.miceAndCheese(reward1 = [1,1], reward2 = [1,1], k = 2), 2)
        self.assertEqual(s.miceAndCheese(reward1 = [3,5], reward2 = [3,5], k = 1), 8)
        self.assertEqual(s.miceAndCheese(reward1 = [1,4,4,6,4], reward2 = [6,5,3,6,1], k = 1), 24)
        self.assertEqual(s.miceAndCheese(reward1 = [1,2,1,2,1,2], reward2 = [2,1,1,2,2,1], k = 0), 9)


if __name__ == '__main__':
    unittest.main()