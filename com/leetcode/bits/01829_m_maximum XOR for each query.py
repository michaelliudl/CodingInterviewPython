from typing import Optional,List,Deque

class Solution:

    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        upperBound = (1 << maximumBit) - 1
        xor = 0
        res = []
        for num in nums:
            xor ^= num
            res.append(xor ^ upperBound)
        res.reverse()
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testSortByBits(self):
        s = Solution()
        self.assertEqual(s.sortByBits(arr = [0,1,2,3,4,5,6,7,8]), [0,1,2,4,8,3,5,6,7])
        self.assertEqual(s.sortByBits(arr = [1024,512,256,128,64,32,16,8,4,2,1]), [1,2,4,8,16,32,64,128,256,512,1024])

if __name__ == '__main__':
    unittest.main()