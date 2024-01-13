from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n<=0 or k<=0:
            return [[]]
        if n<k:
            return [[i for i in range(n)]]
        r,t=[],[]
        self.backtrack(n, k, 1, r, t)
        return r
    
    def backtrack(self, n, k, startIndex, r: list, t: list):
        if len(t)==k:
            r.append(t[:])
            return

        for i in range(startIndex, n+1-(k-len(t))+1):
            t.append(i)
            self.backtrack(n, k, i+1, r, t)
            t.pop()
        

import unittest

class TestSolution(unittest.TestCase):
    def testCombine(self):
        s = Solution()
        self.assertEqual(s.combine(4,2), [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]])
        self.assertEqual(s.combine(1,1), [[1]])
        self.assertEqual(s.combine(5,3), [[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5],[3,4,5]])


if __name__ == '__main__':
    unittest.main()