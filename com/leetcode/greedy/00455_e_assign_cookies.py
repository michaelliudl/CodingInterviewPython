from typing import List

class Solution:

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not g or not s:
            return 0
        g.sort()
        s.sort()
        r,last=0,len(g)-1
        for i in range(len(s)-1,-1,-1):
            for j in range(last,-1,-1):
                if s[i]>=g[j]:
                    r+=1
                    last=j-1
                    break
        return r


import unittest

class TestSolution(unittest.TestCase):
    def testFindContentChildren(self):
        s = Solution()
        self.assertEqual(s.findContentChildren(g = [1,2,3], s = [1,1]), 1)
        self.assertEqual(s.findContentChildren(g = [1,2], s = [1,2,3]), 2)
        


if __name__ == '__main__':
    unittest.main()