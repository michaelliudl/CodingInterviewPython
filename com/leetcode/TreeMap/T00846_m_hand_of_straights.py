from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        pass
    
import unittest

class TestSolution(unittest.TestCase):
    def testFindRedundantConnection(self):
        s = Solution()
        self.assertEqual(s.findRedundantConnection(edges = [[1,2],[1,3],[2,3]]), [2,3])
        self.assertEqual(s.findRedundantConnection(edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]), [1,4])
        # self.assertEqual(s.findRedundantConnection([0,0,0]), [[0,0,0]])


if __name__ == '__main__':
    unittest.main()