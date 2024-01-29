from typing import List

class Solution:

    def balancedStringSplit(self, s: str) -> int:
        if not s: return 0
        rCount,lCount,r=0,0,0
        for c in s:
            if c=='R':
                rCount+=1
            else:
                lCount+=1
            if rCount==lCount:
                r+=1
                rCount,lCount=0,0
        return r

import unittest

class TestSolution(unittest.TestCase):
    def testFindContentChildren(self):
        s = Solution()
        self.assertEqual(s.findContentChildren(g = [1,2,3], s = [1,1]), 1)
        self.assertEqual(s.findContentChildren(g = [1,2], s = [1,2,3]), 2)
        


if __name__ == '__main__':
    unittest.main()