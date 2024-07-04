from typing import List

class Solution:

    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odds = 0
        left = 0
        for i, num in enumerate(arr):
            odds += (1 if num & 1 else 0)
            if i >= 3:
                odds -= (1 if arr[left] & 1 else 0)
                left += 1
            if odds == 3:
                return True
        return False

import unittest

class TestSolution(unittest.TestCase):
    def testMaximumLengthSubstring(self):
        s = Solution()
        self.assertEqual(s.maximumLengthSubstring(s = "bcbbbcba"), 4)
        self.assertEqual(s.maximumLengthSubstring(s = "aaaa"), 2)


if __name__ == '__main__':
    unittest.main()