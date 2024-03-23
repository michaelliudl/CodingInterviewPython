from typing import List

class Solution:

    # Sort by start. Find other start <= current end, also update current end to other end if other end is smaller.
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort()
        result = 1
        burstEnd = points[0][1]
        for i in range(1, len(points)):
            start, end = points[i]
            if start > burstEnd:
                result += 1
                burstEnd = end
            else:
                burstEnd = min(burstEnd, end)
        return result

    # Sort by end position and loop forward. If next start is > current end, means no more overlapping, update end
    def findMinArrowShotsSortByEnd(self, points: List[List[int]]) -> int:
        if not points: return 0
        points.sort(key=lambda p: p[1])
        r,end=1,points[0][1]
        for i in range(1,len(points)):
            if points[i][0]>end:
                r+=1
                end=points[i][1]
        return r




import unittest

class TestSolution(unittest.TestCase):
    def testFindMinArrowShots(self):
        s = Solution()
        self.assertEqual(s.findMinArrowShots(points = [[10,16],[2,8],[1,6],[7,12]]), 2)
        self.assertEqual(s.findMinArrowShots(points = [[1,2],[3,4],[5,6],[7,8]]), 4)
        self.assertEqual(s.findMinArrowShots(points = [[1,2],[2,3],[3,4],[4,5]]), 2)
        self.assertEqual(s.findMinArrowShots(points = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]), 2)
        


if __name__ == '__main__':
    unittest.main()