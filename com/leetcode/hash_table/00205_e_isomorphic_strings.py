from typing import List

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s or not t or len(s)!=len(t): return False
        ds,dt=['']*128,['']*128
        n=len(s)
        for i in range(n):
            sc,tc=s[i],t[i]
            if ds[ord(sc)]=='':
                ds[ord(sc)]=tc
            if dt[ord(tc)]=='':
                dt[ord(tc)]=sc
            if ds[ord(sc)]!=tc or dt[ord(tc)]!=sc:
                return False
        return True


import unittest

class TestSolution(unittest.TestCase):
    def testIsIsomorphic(self):
        s = Solution()
        self.assertEqual(s.isIsomorphic(s = "egg", t = "add"), True)
        self.assertEqual(s.isIsomorphic(s = "foo", t = "bar"), False)
        self.assertEqual(s.isIsomorphic(s = "paper", t = "title"), True)
        self.assertEqual(s.isIsomorphic(s = "badc", t = "baba"), False)
        


if __name__ == '__main__':
    unittest.main()