from typing import List
import math

class Solution:

    # Use sliding window with size of number of 1s, and find max number of 1s in such windows
    # Loop through 2 * len(nums) since circular and mod index by len(nums)
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        totalOnes = nums.count(1)
        left = 0
        winOnes = maxWinOnes = 0    # Number of ones in current window and max so far
        for i in range(n * 2):
            if nums[i % n] == 1:
                winOnes += 1
            if i - left + 1 > totalOnes:    # Window size check
                winOnes -= nums[left % n]   # Decrease if nums[left] is 1
                left += 1
            maxWinOnes = max(maxWinOnes, winOnes)
        return totalOnes - maxWinOnes


import unittest

class TestSolution(unittest.TestCase):
    def testMinSwaps(self):
        s = Solution()
        self.assertEqual(s.minSwaps(nums = [0,1,0,1,1,0,0]), 1)
        self.assertEqual(s.minSwaps(nums = [0,1,1,1,0,0,1,1,0]), 2)
        self.assertEqual(s.minSwaps(nums = [1,1,0,0,1]), 0)


if __name__ == '__main__':
    unittest.main()