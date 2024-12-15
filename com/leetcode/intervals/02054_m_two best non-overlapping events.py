from typing import List

class Solution:

    # Convert start/end to different elements and sort
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        timeList = []   # (time, isStart, value)
        for start, end, value in events:
            timeList.append((start, True, value))
            timeList.append((end + 1, False, value))
        timeList.sort()
        res = maxValue = 0
        for _, isStart, value in timeList:
            if isStart:
                res = max(res, value + maxValue)
            else:
                maxValue = max(maxValue, value)
        return res



import unittest

class TestSolution(unittest.TestCase):
    def testMerge(self):
        s = Solution()
        self.assertEqual(s.merge(intervals = [[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]])
        self.assertEqual(s.merge(intervals = [[1,4],[4,5]]), [[1,5]])
        


if __name__ == '__main__':
    unittest.main()