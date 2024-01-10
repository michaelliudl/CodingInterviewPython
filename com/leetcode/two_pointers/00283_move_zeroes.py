from typing import List

class Solution:

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        s,f=0,0
        while f<len(nums):
            if nums[f]!=0:
                nums[s],nums[f]=nums[f],nums[s]
                s+=1
            f+=1
        return
    
    def moveZeroesAssignZero(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        s=0
        for f in range(len(nums)):
            if nums[f]!=0:
                nums[s]=nums[f]
                s+=1
        for i in range(s,len(nums)):
            nums[i]=0
        return
            
        

    def moveZeroesOld(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        z=-1
        for i in range(len(nums)):
            if nums[i]==0 and (z<0 or nums[z]!=0):
                z=i
            if z>=0 and i!=z and nums[i]!=0:
                nums[i],nums[z]=nums[z],nums[i]
                z+=1
        return
        

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def testMoveZeroes(self):
        nums = [0,1,0,3,12]
        self.s.moveZeroes(nums)
        self.assertEqual(nums, [1,3,12,0,0])

        nums = [0]
        self.s.moveZeroes(nums)
        self.assertEqual(nums, [0])

if __name__ == '__main__':
    unittest.main()