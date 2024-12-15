from typing import List

class Solution:

    # Sort then use sliding window
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        left = 0
        for i in range(len(nums)):
            while nums[i] - nums[left] > 2 * k:
                left += 1
            res = max(res, (i - left + 1))
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