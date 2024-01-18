from typing import List

class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findStart(nums, target):
            low,high,start=0,len(nums)-1,-1
            while low<=high:
                mid=low+(high-low)//2
                if nums[mid]==target:
                    start=mid
                    high=mid-1
                elif nums[mid]>target:
                    high=mid-1
                else:
                    low=mid+1
            return start
        
        def findEnd(nums, target):
            low,high,end=0,len(nums)-1,-1
            while low<=high:
                mid=low+(high-low)//2
                if nums[mid]==target:
                    end=mid
                    low=mid+1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return end
            

        if not nums:
            return [-1,-1]
        return [findStart(nums, target), findEnd(nums, target)]



import unittest

class TestSolution(unittest.TestCase):
    def testSearch(self):
        s = Solution()
        self.assertEqual(s.search([1], 1), 0)
        self.assertEqual(s.search([4,5,6,7,0,1,2], 0), 4)



if __name__ == '__main__':
    unittest.main()