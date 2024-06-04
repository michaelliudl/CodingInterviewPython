from typing import List

class Solution:

    # O(n) solution, count number of elements greater or equal to the elements at each index
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        countGreater = [0] * (n + 1)
        for num in nums:
            if num > n:
                countGreater[n] += 1
            else:
                countGreater[num] += 1
        totalGreater = 0
        for i in range(n, -1, -1):      # Check number of greater elements in reverse order
            totalGreater += countGreater[i]
            if i == totalGreater:
                return i
        return -1
    
    # Sort solution, sort and find the element equals or less than the number of elements greater than it
    def specialArraySort(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        i = 0
        prev = -1
        totalGreater = n
        while i < n:
            if nums[i] == totalGreater or (prev < totalGreater < nums[i]):
                return totalGreater
            prev = nums[i]
            while i + 1 < n and nums[i] == nums[i + 1]:     # Skip subsequent duplicates
                i += 1
            i += 1
            totalGreater = n - i
        return -1

import unittest

class TestSolution(unittest.TestCase):

    def testPivotIndex(self):
        s=Solution()
        self.assertEqual(s.pivotIndex(nums = [1,7,3,6,5,6]), 3)
        self.assertEqual(s.pivotIndex(nums = [2,1,-1]), 0)
        self.assertEqual(s.pivotIndex(nums = [1,2,3]), -1)

if __name__ == '__main__':
    unittest.main()