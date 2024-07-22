from typing import List

class Solution:

    # Simplify code
    def sortColors(self, nums: List[int]) -> None:
        low, high = 0, len(nums) - 1
        mid = 0
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def testSortColors(self):
        input = [2,0,2,1,1,0]
        expected = [0,0,1,1,2,2]
        self.s.sortColors(input)
        self.assertEqual(input, expected)

if __name__ == '__main__':
    unittest.main()