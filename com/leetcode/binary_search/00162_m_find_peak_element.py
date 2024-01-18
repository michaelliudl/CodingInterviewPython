from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums or len(nums)<=1:
            return 0
        low,high=0,len(nums)-1
        # low and high meet at peak
        while low<high:
            mid=low+(high-low)//2
            if nums[mid]<nums[mid+1]:
                low=mid+1
            else:
                high=mid
        return low
            

import unittest

class TestSolution(unittest.TestCase):
    def testTwoSum(self):
        s = Solution()
        self.assertEqual(s.twoSum([2,7,11,15],9), [0,1])
        self.assertEqual(s.twoSum([3,2,4],6), [1,2])
        self.assertEqual(s.twoSum([3,3],6), [0,1])


if __name__ == '__main__':
    unittest.main()