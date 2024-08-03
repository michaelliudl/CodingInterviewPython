from typing import List

class Solution:

    # Same as # 926, use DP to track min number of changes, another variable to track number of larger elements 
    def minimumDeletions(self, s: str) -> int:
        dp = countLarge = 0
        for char in s:
            if char == 'a':     # If smaller, pick min of (changing smaller, or number of larger so far)
                dp = min(dp + 1, countLarge)
            else:
                countLarge += 1
        return dp

import unittest

class TestSolution(unittest.TestCase):
    def testMinFlipsMonoIncr(self):
        s = Solution()
        self.assertEqual(s.minFlipsMonoIncr(s = "00110"), 1)
        self.assertEqual(s.minFlipsMonoIncr(s = "010110"), 2)
        self.assertEqual(s.minFlipsMonoIncr(s = "00011000"), 2)
        


if __name__ == '__main__':
    unittest.main()