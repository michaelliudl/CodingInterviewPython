from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix is None:
            return []
        rm=[]
        t,b,l,r=0,len(matrix),0,len(matrix[0])
        while t<b and l<r:
            for i in range(l,r):
                rm.append(matrix[t][i])
            t+=1
            for i in range(t,b):
                rm.append(matrix[i][r-1])
            r-=1
            if t<b:
                for i in range(r-1,l-1,-1):
                    rm.append(matrix[b-1][i])
                b-=1
            if l<r:
                for i in range(b-1,t-1,-1):
                    rm.append(matrix[i][l])
                l+=1
        return rm

import unittest

class TestSolution(unittest.TestCase):
    def testSpiralOrder(self):
        s = Solution()
        self.assertEqual(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]), [1,2,3,6,9,8,7,4,5])
        self.assertEqual(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]), [1,2,3,4,8,12,11,10,9,5,6,7])
        self.assertEqual(s.spiralOrder([[1,2,3]]), [1,2,3])

if __name__ == '__main__':
    unittest.main()