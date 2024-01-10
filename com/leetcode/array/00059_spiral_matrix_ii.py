from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n<=0:
            return [[]]
        ret=[[None]*n for _ in range(n)]
        t,b,l,r,c=0,n,0,n,1
        while t<b and l<r:
            for i in range(l,r):
                ret[t][i]=c
                c+=1
            t+=1
            for i in range(t,b):
                ret[i][r-1]=c
                c+=1
            r-=1
            for i in range(r-1,l-1,-1):
                ret[b-1][i]=c
                c+=1
            b-=1
            for i in range(b-1,t-1,-1):
                ret[i][l]=c
                c+=1
            l+=1
        return ret


import unittest

class TestSolution(unittest.TestCase):
    def testGenerateMatrix(self):
        s = Solution()
        self.assertEqual(s.generateMatrix(0), [[]])
        self.assertEqual(s.generateMatrix(1), [[1]])
        self.assertEqual(s.generateMatrix(2), [[1,2],[4,3]])
        self.assertEqual(s.generateMatrix(3), [[1,2,3],[8,9,4],[7,6,5]])


if __name__ == '__main__':
    unittest.main()