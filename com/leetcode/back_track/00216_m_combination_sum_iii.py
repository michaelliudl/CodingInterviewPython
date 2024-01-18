from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(k, n, start, r: list, path: list):
            if len(path)==k:
                if sum(path)==n:
                    r.append(path[:])
                return
            for i in range(start, (9+1)-(k-len(path))+1):
                path.append(i)
                if sum(path)<=n:
                    backtrack(k, n, i+1, r, path)
                path.pop()

        if n<=0 or k<=0 or k>9:
            return []
        r=[]
        backtrack(k, n, 1, r=r, path=[])
        return r
        
        

import unittest

class TestSolution(unittest.TestCase):
    def testCombine(self):
        s = Solution()
        self.assertEqual(s.combine(4,2), [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]])
        self.assertEqual(s.combine(1,1), [[1]])
        self.assertEqual(s.combine(5,3), [[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5],[3,4,5]])


if __name__ == '__main__':
    unittest.main()