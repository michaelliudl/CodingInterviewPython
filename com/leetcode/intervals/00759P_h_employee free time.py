from typing import List

'''
We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.
'''

class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

class Solution:

    # Sort by start and check overlap, update end if overlap
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        if not schedule:
            return []
        workTimes = []
        for intervalList in schedule:
            for interval in intervalList:
                workTimes.append((interval.start, interval.end))
        workTimes.sort()
        end = workTimes[0][1]
        result = []
        for i in range(1, len(workTimes)):
            curStart, curEnd = workTimes[i]
            if curStart > end:
                result.append(Interval(end, curStart))
                end = curEnd
            else:
                end = max(end, curEnd)
        return result




import unittest

class TestSolution(unittest.TestCase):
    def testIntervalIntersection(self):
        s = Solution()
        self.assertEqual(s.intervalIntersection(firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]), 
                         [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]])
        self.assertEqual(s.intervalIntersection(firstList = [[1,3],[5,9]], secondList = []), [])



if __name__ == '__main__':
    unittest.main()