from typing import List
import heapq, math

class Solution:
    
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counts = Counter(s)
        heap = [(-ord(char), count) for char, count in counts.items()]
        heapq.heapify(heap)
        res = []
        while heap:
            char, count = heapq.heappop(heap)
            for _ in range(min(count, repeatLimit)):
                res.append(chr(-char))
            if count > repeatLimit:
                if not heap:
                    break
                nextChar, nextCount = heapq.heappop(heap)
                res.append(chr(-nextChar))
                if nextCount > 1:
                    heapq.heappush(heap, (nextChar, nextCount - 1))
                heapq.heappush(heap, (char, count - repeatLimit))
        return ''.join(res)


import unittest

class TestSolution(unittest.TestCase):
    def testLastStoneWeight(self):
        s = Solution()
        self.assertEqual(s.lastStoneWeight(stones = [2,7,4,1,8,1]), 1)
        self.assertEqual(s.lastStoneWeight(stones=[1]), 1)



if __name__ == '__main__':
    unittest.main()