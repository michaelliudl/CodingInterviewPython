from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if not nums or len(nums) < 3: return -1
        nums.sort()
        total = sum(nums)
        for i in range(len(nums)-1, 1, -1):
            if total - nums[i] > nums[i]:
                return total
            total -= nums[i]
        return -1


import unittest

class TestSolution(unittest.TestCase):
    def testRearrangeArray(self):
        s = Solution()
        self.assertEqual(s.rearrangeArray(nums = [3,1,-2,-5,2,-4]), [3,-2,1,-5,2,-4])
        self.assertEqual(s.rearrangeArray(nums = [-1,1]), [1,-1])

if __name__ == '__main__':
    unittest.main()