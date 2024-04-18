from typing import List

class Solution:

    def countHillValley(self, nums: List[int]) -> int:

        def hill(i):
            return nums[i] > prev and nums[i] > nums[i + 1]
        
        def valley(i):
            return nums[i] < prev and nums[i] < nums[i + 1]

        if not nums or len(nums) < 3:
            return 0
        result = 0
        prev = nums[0]                      # Prev hill top or valley bottom
        for i in range(1, len(nums) - 1):
            if hill(i) or valley(i):
                result += 1
                prev = nums[i]              # Update only at last element of hill top or valley bottom
        return result

        

import unittest

class TestSolution(unittest.TestCase):

    def testCanPlaceFlowers(self):
        s=Solution()
        self.assertEqual(s.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1), True)
        self.assertEqual(s.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2), False)
        self.assertEqual(s.canPlaceFlowers(flowerbed = [0], n = 1), True)

if __name__ == '__main__':
    unittest.main()