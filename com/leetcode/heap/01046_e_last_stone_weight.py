from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        if len(stones)<2:
            return stones[0]
        h=[-stone for stone in stones]
        heapq.heapify(h)
        while h and len(h)>1:
            l=-heapq.heappop(h)
            sl=-heapq.heappop(h)
            if l-sl>0:
                heapq.heappush(h,sl-l)
        return 0 if not h else -h[0]
        



import unittest

class TestSolution(unittest.TestCase):
    def testLastStoneWeight(self):
        s = Solution()
        self.assertEqual(s.lastStoneWeight(stones = [2,7,4,1,8,1]), 1)
        self.assertEqual(s.lastStoneWeight(stones=[1]), 1)



if __name__ == '__main__':
    unittest.main()