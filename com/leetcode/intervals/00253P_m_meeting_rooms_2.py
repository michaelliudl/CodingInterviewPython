from typing import List
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort()
        result = 1
        heap = [intervals[0][1]]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if heap and start < heap[0]:
                result += 1
            elif heap:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
        return result


import unittest

class TestSolution(unittest.TestCase):
    def testMinMeetingRooms(self):
        s = Solution()
        self.assertEqual(s.minMeetingRooms(intervals = [[0,30],[5,10],[15,20]]), 2)
        self.assertEqual(s.minMeetingRooms(intervals = [[7,10],[2,4]]), 1)


if __name__ == '__main__':
    unittest.main()