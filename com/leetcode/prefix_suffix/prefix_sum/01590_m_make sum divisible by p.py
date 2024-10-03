from typing import List

class Solution:

    # Use map to track count of prefix sum values divisible by `p`
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        if total % p == 0:
            return 0
        res = len(nums)
        prefixSum = 0
        prefixIndex = {0: -1}
        for index, num in enumerate(nums):
            prefixSum += num
            prefixSum %= p
            diff = (prefixSum - (total % p) + p) % p
            if diff in prefixIndex:
                res = min(res, (index - prefixIndex[diff]))
            prefixIndex[prefixSum] = index
        if res == len(nums):
            return -1
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testNumSubarraysWithSum(self):
        s = Solution()
        self.assertEqual(s.checkSubarraySum(nums = [5,0,0,0], k = 3), True)
        self.assertEqual(s.checkSubarraySum(nums = [0,1,0,3,0,4,0,4,0], k = 5), False)
        self.assertEqual(s.checkSubarraySum(nums = [23,2,4,6,7], k = 6), True)
        self.assertEqual(s.checkSubarraySum(nums = [23,2,6,4,7], k = 6), True)
        self.assertEqual(s.checkSubarraySum(nums = [23,2,6,4,7], k = 13), False)


if __name__ == '__main__':
    unittest.main()