from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        def find(x):
            if x==uf[x]:
                return x
            uf[x]=find(uf[x])
            return uf[x]

        def same(u,v):
            ufU=find(u)
            ufV=find(v)
            return ufU==ufV
        
        def join(u,v):
            ufU=find(u)
            ufV=find(v)
            if ufU==ufV: return
            uf[ufV]=ufU

        if not edges:
            return []
        n=len(edges)
        uf=[i for i in range(n+1)]
        for e in edges:
            u,v=e
            if same(u,v):
                return e
            else:
                join(u,v)
        return []


import unittest

class TestSolution(unittest.TestCase):
    def testFindRedundantConnection(self):
        s = Solution()
        self.assertEqual(s.findRedundantConnection(edges = [[1,2],[1,3],[2,3]]), [2,3])
        self.assertEqual(s.findRedundantConnection(edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]), [1,4])
        # self.assertEqual(s.findRedundantConnection([0,0,0]), [[0,0,0]])


if __name__ == '__main__':
    unittest.main()