from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums: return -1
        low, high=0, len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] < nums[high]:
                high=mid
            else:
                low=mid+1
        return nums[low]
            

import unittest

class TestSolution(unittest.TestCase):
    def testFindMin(self):
        s = Solution()
        self.assertEqual(s.findMin(nums = [2,1]), 1)
        self.assertEqual(s.findMin(nums = [3,4,5,1,2]), 1)
        self.assertEqual(s.findMin(nums = [4,5,6,7,0,1,2]), 0)
        self.assertEqual(s.findMin(nums = [11,13,15,17]), 11)


if __name__ == '__main__':
    unittest.main()