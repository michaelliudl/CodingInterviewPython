from typing import List

class Solution:
    # [low, high]
    def search(self, nums: List[int], target: int) -> int:    
        if not nums:
            return -1
        low,high=0,len(nums)-1
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return -1
    
    # [low, high)
    def search1(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        low,high=0,len(nums)
        while low<high:
            mid=low+(high-low)//2
            if nums[mid]>target:
                high=mid
            elif nums[mid]<target:
                low=mid+1
            else:
                return mid
        return -1


import unittest

class TestSolution(unittest.TestCase):
    def testTwoSum(self):
        s = Solution()
        self.assertEqual(s.twoSum([2,7,11,15],9), [0,1])
        self.assertEqual(s.twoSum([3,2,4],6), [1,2])
        self.assertEqual(s.twoSum([3,3],6), [0,1])


if __name__ == '__main__':
    unittest.main()