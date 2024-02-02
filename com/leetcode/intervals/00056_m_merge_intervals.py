from typing import List

class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or len(intervals)==1:
            return intervals
        intervals.sort()
        r,start,end,n=[],intervals[0][0],intervals[0][1],len(intervals)
        for i in range(1,n):
            curS,curE=intervals[i]
            if curS>end:
                r.append([start,end])
                start,end=curS,curE
            else:
                end=max(end,curE)
        r.append([start,end])
        return r



import unittest

class TestSolution(unittest.TestCase):
    def testMerge(self):
        s = Solution()
        self.assertEqual(s.merge(intervals = [[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]])
        self.assertEqual(s.merge(intervals = [[1,4],[4,5]]), [[1,5]])
        


if __name__ == '__main__':
    unittest.main()