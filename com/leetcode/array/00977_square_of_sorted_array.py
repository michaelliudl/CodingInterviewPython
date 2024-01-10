from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums is None:
            return None
        r = [None]*len(nums)
        low, high = 0, len(nums) - 1
        k = high
        while low<=high:
            if nums[low]*nums[low]<=nums[high]*nums[high]:
                r[k]=nums[high]*nums[high]
                high-=1
                k-=1
            else:
                r[k]=nums[low]*nums[low]
                low+=1
                k-=1
        return r
        

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def testSortedSquares(self):
        self.assertEqual(self.s.sortedSquares([-4,-1,0,3,10]), [0,1,9,16,100])
        self.assertEqual(self.s.sortedSquares([-7,-3,2,3,11]), [4,9,9,49,121])

if __name__ == '__main__':
    unittest.main()