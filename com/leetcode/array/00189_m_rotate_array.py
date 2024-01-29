from typing import List

class Solution:

    # Option 1. O(k) space copy, O(n) time
    # Option 2. O(1) space copy, O(k*n) time
    # Option 3. Reverse k, reverse n-k, reverse n. O(1) space, O(k+n) time
    # Mod k by n
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(low,high):
            while low<high:
                nums[low],nums[high]=nums[high],nums[low]
                low+=1
                high-=1

        if not nums or k<=0: return
        n=len(nums)
        k%=n
        reverse(low=(n-k),high=(n-1))
        reverse(low=0,high=(n-k-1))
        reverse(low=0,high=n-1)


        

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def testSortedSquares(self):
        self.assertEqual(self.s.sortedSquares([-4,-1,0,3,10]), [0,1,9,16,100])
        self.assertEqual(self.s.sortedSquares([-7,-3,2,3,11]), [4,9,9,49,121])

if __name__ == '__main__':
    unittest.main()