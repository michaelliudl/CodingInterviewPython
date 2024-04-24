from typing import List

class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 0:
            return n
        if n in (1, 2):
            return 1
        t0 = 0
        t1 = t2 = 1
        t = 0
        for i in range(3, n + 1):
            t = t2 + t1 + t0
            t0 = t1
            t1 = t2
            t2 = t
        return t

import unittest

class TestSolution(unittest.TestCase):
    def testThreeSum(self):
        s = Solution()
        self.assertEqual(s.threeSum([-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]])
        self.assertEqual(s.threeSum([0,1,1]), [])
        self.assertEqual(s.threeSum([0,0,0]), [[0,0,0]])


if __name__ == '__main__':
    unittest.main()