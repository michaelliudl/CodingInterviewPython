from typing import List

class Solution:

    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        low,high=0,len(nums)-1
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>=nums[low]:
                if target<=nums[mid] and target>=nums[low]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if target>=nums[mid] and target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        return -1
        
        





import unittest

class TestSolution(unittest.TestCase):
    def testSearch(self):
        s = Solution()
        self.assertEqual(s.search([1], 1), 0)
        self.assertEqual(s.search([4,5,6,7,0,1,2], 0), 4)



if __name__ == '__main__':
    unittest.main()