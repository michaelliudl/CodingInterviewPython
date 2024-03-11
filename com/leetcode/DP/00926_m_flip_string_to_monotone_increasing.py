from typing import List

class Solution:

    def minFlipsMonoIncr(self, s: str) -> int:
        if not s:
            return 0
        dp = 0              # Track min # of flips
        onesCount = 0       # Track # of zeros
        for ch in s:
            if ch == '0':
                # 1. Flip '0' to '1' and increase dp count
                # 2. Flip all '1's before this '0'
                dp = min(dp + 1, onesCount)
            else:
                onesCount += 1
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