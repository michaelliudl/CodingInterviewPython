from typing import Optional,List,Deque

class Solution:

    def singleNumber(self, nums: List[int]) -> List[int]:
        xorAll = 0      # XOR all results in XOR of 2 distinct numbers
        for num in nums:
            xorAll ^= num
        # We can use a number that has one bit as `1` from `xorAll`
        lowestOneBit = (xorAll & -xorAll)   # This results in a number with lowest bit with `1` from `xorAll`, since `-` inverses all bits then add `1`
        # Separate array into two groups with `loestOneBit` as `0` and `1` respectively
        # Results appear in each group once respectively
        res1 = res2 = 0
        for num in nums:
            if num & lowestOneBit:
                res1 ^= num
            else:
                res2 ^= num
        return [res1, res2]

import unittest

class TestSolution(unittest.TestCase):
    def testSortByBits(self):
        s = Solution()
        self.assertEqual(s.sortByBits(arr = [0,1,2,3,4,5,6,7,8]), [0,1,2,4,8,3,5,6,7])
        self.assertEqual(s.sortByBits(arr = [1024,512,256,128,64,32,16,8,4,2,1]), [1,2,4,8,16,32,64,128,256,512,1024])

if __name__ == '__main__':
    unittest.main()