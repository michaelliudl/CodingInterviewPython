from typing import List

class Solution:

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        uf=[i for i in range(n)]

        def find(u):
            if u==uf[u]:
                return u
            uf[u]=find(uf[u])
            return uf[u]
        
        def same(u,v):
            ufU=find(u)
            ufV=find(v)
            return ufU==ufV
        
        def join(u,v):
            ufU=find(u)
            ufV=find(v)
            if ufU==ufV: return
            uf[ufV]=ufU

        if n<=0 or source<0 or destination<0:
            return False
        if source==destination:
            return True
        for u,v in edges:
            join(u,v)
        return same(source,destination)




    # Timeout
    def validPathDFS(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n<=0 or source<0 or destination<0:
            return False
        if source==destination:
            return True
        d={}
        for u,v in edges:
            if u in d:
                d[u].append(v)
            else:
                d[u]=[v]
            if v in d:
                d[v].append(u)
            else:
                d[v]=[u]
        st=[source]
        visited=[]
        while st:
            cur=st.pop()
            visited.append(cur)
            if cur==destination:
                return True
            if not cur in d:
                return False
            for next in d[cur]:
                if  not next in visited:
                    st.append(next)
        return False


import unittest

class TestSolution(unittest.TestCase):
    def testValidPath(self):
        s = Solution()
        self.assertEqual(s.validPath(n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2), True)
        self.assertEqual(s.validPath(n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5), False)
        # self.assertEqual(s.validPath(n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2), True)


if __name__ == '__main__':
    unittest.main()