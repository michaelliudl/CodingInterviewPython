from typing import List
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        if not s or len(s)<=1: return s
        counter = {}
        for c in s:
            counter[c] = counter.get(c,0) + 1
        heap = []
        for k,v in counter.items():
            heapq.heappush(heap, (-v, k))
        lastChar,lastFreq,ans = None,0,[]
        while heap:
            freq, ch = heapq.heappop(heap)      # Pop out most frequent char, next round will get second frequent
            if ans and ans[-1] == ch:
                return ''
            ans.append(ch)
            if lastFreq < 0:                    # Push back previous most frequent char
                heapq.heappush(heap, (lastFreq, lastChar))
            lastFreq = freq + 1
            lastChar = ch
        if len(ans) != len(s): return ''
        return ''.join(ans)


import unittest

class TestSolution(unittest.TestCase):
    def testKClosest(self):
        s = Solution()
        self.assertEqual(sorted(s.kClosest(points = [[1,3],[-2,2]], k = 1)), sorted([[-2,2]]))
        self.assertEqual(sorted(s.kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2)), sorted([[3,3],[-2,4]]))



if __name__ == '__main__':
    unittest.main()