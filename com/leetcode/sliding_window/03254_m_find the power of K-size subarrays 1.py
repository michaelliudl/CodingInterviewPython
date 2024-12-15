from typing import List

class Solution:

    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        left = 0
        for index, num in enumerate(nums):
            if index > 0 and num != (nums[index - 1] + 1):  # Check if consecutive and ascending, otherwise reset
                left = index
            if index >= (k - 1):
                res.append(num if (index - left + 1) >= k else -1)  # Check if consecutive and ascending subarray is at least length `k`
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