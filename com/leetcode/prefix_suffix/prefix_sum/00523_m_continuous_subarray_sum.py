from typing import List

class Solution:

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if not nums or len(nums) < 2: return False
        # Prefix sum and cache remainder of mod(k) in map
        map = {0: -1}
        curSum = 0
        for i, num in enumerate(nums):
            curSum += num
            remainder = curSum % k
            if remainder in map:
                if (i - map[remainder]) > 1:
                    return True
            else:
                map[remainder] = i
        return False
        

import unittest

class TestSolution(unittest.TestCase):
    def testCheckSubarraySum(self):
        s = Solution()
        self.assertEqual(s.checkSubarraySum(nums = [5,0,0,0], k = 3), True)
        self.assertEqual(s.checkSubarraySum(nums = [0,1,0,3,0,4,0,4,0], k = 5), False)
        self.assertEqual(s.checkSubarraySum(nums = [23,2,4,6,7], k = 6), True)
        self.assertEqual(s.checkSubarraySum(nums = [23,2,6,4,7], k = 6), True)
        self.assertEqual(s.checkSubarraySum(nums = [23,2,6,4,7], k = 13), False)


if __name__ == '__main__':
    unittest.main()