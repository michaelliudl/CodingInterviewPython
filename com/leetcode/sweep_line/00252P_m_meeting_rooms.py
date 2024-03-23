from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort()
        for i in range(1, len(intervals)):
            prevEnd = intervals[i - 1][1]
            start = intervals[i][0]
            if start < prevEnd:
                return False
        return True


import unittest

class TestSolution(unittest.TestCase):
    def testCanAttendMeetings(self):
        s = Solution()
        self.assertEqual(s.canAttendMeetings(intervals = [[0,30],[5,10],[15,20]]), False)
        self.assertEqual(s.canAttendMeetings(intervals = [[7,10],[2,4]]), True)


if __name__ == '__main__':
    unittest.main()