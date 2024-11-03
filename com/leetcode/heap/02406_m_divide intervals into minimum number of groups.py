from typing import List
import heapq

class Solution:

    # Similar to #253 meeting rooms 2
    # Sort intervals by `start`, use min heap to track `end`s
    def minGroups(self, intervals: List[List[int]]) -> int:
        heap = []
        intervals.sort()
        for start, end in intervals:
            if heap and start > heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
        return len(heap)


import unittest

class TestSolution(unittest.TestCase):
    def testTopKFrequent(self):
        s = Solution()
        self.assertEqual(s.topKFrequent(words = ["i","love","leetcode","i","love","coding"], k = 2), ["i","love"])
        self.assertEqual(s.topKFrequent(words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4), ["the","is","sunny","day"])



if __name__ == '__main__':
    unittest.main()