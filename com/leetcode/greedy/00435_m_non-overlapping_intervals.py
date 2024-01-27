from typing import List

class Solution:

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals or len(intervals)<=1:
            return 0
        intervals.sort(key=lambda x: x[1])
        r,end=0,intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0]<end:
                r+=1
            else:
                end=intervals[i][1]
        return r




import unittest

class TestSolution(unittest.TestCase):
    def testEraseOverlapIntervals(self):
        s = Solution()
        self.assertEqual(s.eraseOverlapIntervals(intervals = [[1,2],[2,3],[3,4],[1,3]]), 1)
        self.assertEqual(s.eraseOverlapIntervals(intervals = [[1,2],[1,2],[1,2]]), 2)
        self.assertEqual(s.eraseOverlapIntervals(intervals = [[1,2],[2,3]]), 0)
        


if __name__ == '__main__':
    unittest.main()