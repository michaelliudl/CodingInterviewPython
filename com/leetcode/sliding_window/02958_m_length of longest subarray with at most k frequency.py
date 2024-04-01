from typing import List

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        if not nums:
            return 0
        numCount = {}
        left = 0
        result = 0
        for i, num in enumerate(nums):
            numCount[num] = numCount.get(num, 0) + 1
            while numCount[num] > k:                    # Only need to check newly added number's frequency, not all frequencies
                out = nums[left]
                numCount[out] -= 1
                left += 1
            result = max(result, i - left + 1)
        return result
    
import unittest

class TestSolution(unittest.TestCase):
    def testMaxSubarrayLength(self):
        s = Solution()
        self.assertEqual(s.maxSubarrayLength(nums = [1,2,3,1,2,3,1,2], k = 2), 6)
        self.assertEqual(s.maxSubarrayLength(nums = [1,2,1,2,1,2,1,2], k = 1), 2)
        self.assertEqual(s.maxSubarrayLength(nums = [5,5,5,5,5,5,5], k = 4), 4)


if __name__ == '__main__':
    unittest.main()