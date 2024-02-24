from typing import Optional,List,Deque


class Solution:

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shiftedBits = 0
        while left != right:
            left >>= 1
            right >>= 1
            shiftedBits += 1
        return left << shiftedBits

import unittest

class TestSolution(unittest.TestCase):
    def testSortByBits(self):
        s = Solution()
        self.assertEqual(s.sortByBits(arr = [0,1,2,3,4,5,6,7,8]), [0,1,2,4,8,3,5,6,7])
        self.assertEqual(s.sortByBits(arr = [1024,512,256,128,64,32,16,8,4,2,1]), [1,2,4,8,16,32,64,128,256,512,1024])

if __name__ == '__main__':
    unittest.main()