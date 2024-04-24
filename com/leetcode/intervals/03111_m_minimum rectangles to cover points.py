from typing import List

class Solution:

    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        if not points:
            return 0
        points.sort()
        start = points[0][0]
        ret = 1
        for i in range(1, len(points)):
            if points[i][0] > start + w:
                ret += 1
                start = points[i][0]
        return ret



import unittest

class TestSolution(unittest.TestCase):
    def testMerge(self):
        s = Solution()
        self.assertEqual(s.merge(intervals = [[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]])
        self.assertEqual(s.merge(intervals = [[1,4],[4,5]]), [[1,5]])
        


if __name__ == '__main__':
    unittest.main()