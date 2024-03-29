from typing import List

class Solution:

    # For loop
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals
        result = []
        newStart, newEnd = newInterval
        insertStart, insertEnd = newStart, newEnd
        inserted = False
        for index, interval in enumerate(intervals):
            start, end = interval
            if end < newStart:
                result.append(interval)
            elif end >= newStart and start <= newEnd:
                insertStart = min(insertStart, start)
                insertEnd = max(insertEnd, end)
            elif start > newEnd:
                if not inserted:
                    result.append([insertStart, insertEnd])
                    inserted = True
                result.append(interval)
        if not inserted:
            result.append([insertStart, insertEnd])
        return result

    # While loop
    def insertWhile(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not newInterval: return intervals
        start,end=newInterval
        startMerge,endMerge=newInterval
        r=[]
        i,n=0,len(intervals)
        while i<n:
            curStart,curEnd=intervals[i]
            if curEnd<start:
                r.append([curStart,curEnd])
                i+=1
            else:
                break
        while i<n:
            curStart,curEnd=intervals[i]
            if curStart<=end:
                startMerge=min(startMerge,curStart)
                endMerge=max(endMerge,curEnd)
                i+=1
            else:
                break
        r.append([startMerge,endMerge])
        while i<n:
            r.append(intervals[i])
            i+=1
        return r

        

        

import unittest

class TestSolution(unittest.TestCase):

    def testInsert(self):
        s=Solution()
        self.assertEqual(s.insert(intervals = [], newInterval = [5,7]), [[5,7]])
        self.assertEqual(s.insert(intervals = [[1,3],[6,9]], newInterval = [2,5]), [[1,5],[6,9]])
        self.assertEqual(s.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]), [[1,2],[3,10],[12,16]])

if __name__ == '__main__':
    unittest.main()