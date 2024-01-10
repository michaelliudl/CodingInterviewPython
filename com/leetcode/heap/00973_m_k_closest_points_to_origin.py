from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points or k<=0 or len(points)<=k:
            return points
        h=[]
        r=[]
        for p in points:
            dist=-(p[0]*p[0]+p[1]*p[1])
            t=(dist, p)
            if len(h)<k:
                heapq.heappush(h,t)
            elif dist>h[0][0]:
                heapq.heappop(h)
                heapq.heappush(h,t)
        for t in h:
            r.append(t[1])
        return r

import unittest

class TestSolution(unittest.TestCase):
    def testKClosest(self):
        s = Solution()
        self.assertEqual(sorted(s.kClosest(points = [[1,3],[-2,2]], k = 1)), sorted([[-2,2]]))
        self.assertEqual(sorted(s.kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2)), sorted([[3,3],[-2,4]]))



if __name__ == '__main__':
    unittest.main()