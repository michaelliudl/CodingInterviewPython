from typing import List
import heapq

class Solution:
    def largestPalindromic(self, num: str) -> str:
        if not num:
            return num
        numCounts = {}
        for i in num:
            numCounts[int(i)] = numCounts.get(int(i), 0) + 1
        heap = []
        oneCountHeap = []
        for i, count in numCounts.items():
            if count == 1:
                heapq.heappush(oneCountHeap, -i)
            elif count % 2 == 0:
                heapq.heappush(heap, (-i, count))
            else:
                heapq.heappush(oneCountHeap, -i)
                heapq.heappush(heap, (-i, count - 1))
        while heap and heap[0][0] == 0:
            heapq.heappop(heap)
        resultLen = sum(count for _, count in heap)
        resultLen += 1 if oneCountHeap else 0
        result = [''] * resultLen
        index = 0
        while heap:
            n, count = heapq.heappop(heap)
            for i in range(count // 2):
                result[index + i] = result[resultLen - 1 - index - i] = str(-n)
            index += count // 2
        if oneCountHeap:
            result[index] = str(-heapq.heappop(oneCountHeap))
        return ''.join(result) if result else '0'


import unittest

class TestSolution(unittest.TestCase):
    def testLastStoneWeight(self):
        s = Solution()
        self.assertEqual(s.lastStoneWeight(stones = [2,7,4,1,8,1]), 1)
        self.assertEqual(s.lastStoneWeight(stones=[1]), 1)



if __name__ == '__main__':
    unittest.main()