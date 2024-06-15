from typing import Optional,List,Deque

class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        ones = 0    # Bits appeared one time 
        twos = 0    # Bits appeared two times
        for num in nums:
            ones ^= (num & ~twos)   # Update bits already appeared two times back to one
            twos ^= (num & ~ones)   # Update bits appeared one time to two
        return ones

import unittest

class TestSolution(unittest.TestCase):
    def testSortByBits(self):
        s = Solution()
        self.assertEqual(s.sortByBits(arr = [0,1,2,3,4,5,6,7,8]), [0,1,2,4,8,3,5,6,7])
        self.assertEqual(s.sortByBits(arr = [1024,512,256,128,64,32,16,8,4,2,1]), [1,2,4,8,16,32,64,128,256,512,1024])

if __name__ == '__main__':
    unittest.main()