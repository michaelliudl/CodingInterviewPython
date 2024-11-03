from typing import List

class Solution:

    # Loop and count `1`s so far. For each `0`, add count of `1`s to result
    def minimumSteps(self, s: str) -> int:
        res = ones = 0
        for char in s:
            if char == '1':
                ones += 1
            else:
                res += ones
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testCanJump(self):
        s = Solution()
        self.assertEqual(s.canJump(nums = [2,3,1,1,4]), True)
        self.assertEqual(s.canJump(nums = [3,2,1,0,4]), False)
        


if __name__ == '__main__':
    unittest.main()