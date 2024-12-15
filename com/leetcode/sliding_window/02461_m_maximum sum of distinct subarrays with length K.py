from typing import List, DefaultDict

class Solution:

    # Use fixed size sliding window to track distinct numbers and sum of subarray
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        counts = DefaultDict(int)
        subarrSum = 0
        distinct = 0
        res = 0
        for index, num in enumerate(nums):
            subarrSum += num
            counts[num] += 1
            if counts[num] == 1:
                distinct += 1
            if index >= k:
                out = nums[index - k]
                counts[out] -= 1
                if counts[out] == 0:
                    distinct -= 1
                subarrSum -= out
            if distinct == k:
                res = max(res, subarrSum)
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testminWindow(self):
        s = Solution()
        self.assertEqual(s.minWindow(s = "ADOBECODEBANC", t = "ABC"), "BANC")
        self.assertEqual(s.minWindow(s = "a", t = "a"), 'a')
        self.assertEqual(s.minWindow(s = "a", t = "aa"), '')


if __name__ == '__main__':
    unittest.main()