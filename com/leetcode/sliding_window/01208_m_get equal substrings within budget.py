from typing import List
import math

class Solution:

    # Equvalent to having a diff array and find longest subarray sum <= maxCost
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost = res = left = 0
        for i in range(len(s)):
            cost += abs(ord(s[i]) - ord(t[i]))
            while cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            res = max(res, i - left + 1)
        return res


import unittest

class TestSolution(unittest.TestCase):
    def testMinimumSubarrayLength(self):
        s = Solution()
        self.assertEqual(s.minimumSubarrayLength(nums = [1,2], k = 0), 1)
        self.assertEqual(s.minimumSubarrayLength(nums = [1,2,3], k = 2), 1)
        self.assertEqual(s.minimumSubarrayLength(nums = [2,1,8], k = 10), 3)
        self.assertEqual(s.minimumSubarrayLength(nums = [16,1,2,20,32], k = 45), 2)


if __name__ == '__main__':
    unittest.main()