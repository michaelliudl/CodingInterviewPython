from typing import List
class Solution:

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        # Find first non ascending index from beginning
        nonAsc = 0
        while nonAsc < n - 1:
            if nums[nonAsc] > nums[nonAsc + 1]:
                break
            nonAsc += 1
        # Find first non descending index from end
        nonDesc = n - 1
        while nonDesc > 0:
            if nums[nonDesc] < nums[nonDesc - 1]:
                break
            nonDesc -= 1
        # nonAsc should be less than nonDesc unless all sorted
        if nonAsc >= nonDesc:
            return 0
        # Find min, max values in range [nonAsc, nonDesc]
        minVal, maxVal = float('inf'), -float('inf')
        for i in range(nonAsc, nonDesc + 1):
            minVal = min(minVal, nums[i])
            maxVal = max(maxVal, nums[i])
        # Find first index greater than minVal from beginning
        left = 0
        while left < n and nums[left] <= minVal:
            left += 1
        # Find last index less than maxVal from end
        right = n - 1
        while right >= 0 and nums[right] >= maxVal:
            right -= 1
        return right - left + 1



import unittest

class TestSolution(unittest.TestCase):
    def testFourSum(self):
        s = Solution()
        self.assertEqual(s.fourSum(nums = [-3,-1,0,2,4,5], target = 2), [[-3,-1,2,4]])
        self.assertEqual(s.fourSum(nums = [-3,-1,0,2,4,5], target = 1), [[-3,-1,0,5]])
        self.assertEqual(s.fourSum(nums = [-2,-1,-1,1,1,2,2], target = 0), [[-2,-1,1,2],[-1,-1,1,1]])
        self.assertEqual(s.fourSum(nums = [1,0,-1,0,-2,2], target = 0), [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]])
        self.assertEqual(s.fourSum(nums = [2,2,2,2,2], target = 8), [[2,2,2,2]])


if __name__ == '__main__':
    unittest.main()