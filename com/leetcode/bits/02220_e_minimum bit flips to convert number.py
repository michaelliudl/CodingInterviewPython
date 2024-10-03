from typing import Optional,List,Deque

class Solution:

    def minBitFlips(self, start: int, goal: int) -> int:
        res = 0
        for _ in range(32):
            if (start & 1 == 1 and goal & 1 == 0) or (start & 1 == 0 and goal & 1 == 1):
                res += 1
            start >>= 1
            goal >>= 1
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testSortByBits(self):
        s = Solution()
        self.assertEqual(s.sortByBits(arr = [0,1,2,3,4,5,6,7,8]), [0,1,2,4,8,3,5,6,7])
        self.assertEqual(s.sortByBits(arr = [1024,512,256,128,64,32,16,8,4,2,1]), [1,2,4,8,16,32,64,128,256,512,1024])

if __name__ == '__main__':
    unittest.main()