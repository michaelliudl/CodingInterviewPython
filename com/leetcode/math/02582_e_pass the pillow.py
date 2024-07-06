from typing import List

class Solution:

    # (n - 1) forward and (n - 1) backward
    def passThePillow(self, n: int, time: int) -> int:
        time %= 2 * (n - 1)
        if time < n:
            return time + 1
        else:
            return (n - (time - (n - 1)))

import unittest

class TestSolution(unittest.TestCase):
    def testThreeSum(self):
        s = Solution()
        self.assertEqual(s.threeSum([-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]])
        self.assertEqual(s.threeSum([0,1,1]), [])
        self.assertEqual(s.threeSum([0,0,0]), [[0,0,0]])


if __name__ == '__main__':
    unittest.main()