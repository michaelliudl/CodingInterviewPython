from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        if not arr: return False
        d={}
        for a in arr:
            if a in d:
                d[a]+=1
            else:
                d[a]=1
        d1={}
        for k,v in d.items():
            if v in d1:
                return False
            else:
                d1[v]=k
        return True

        

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def testSortedSquares(self):
        self.assertEqual(self.s.sortedSquares([-4,-1,0,3,10]), [0,1,9,16,100])
        self.assertEqual(self.s.sortedSquares([-7,-3,2,3,11]), [4,9,9,49,121])

if __name__ == '__main__':
    unittest.main()