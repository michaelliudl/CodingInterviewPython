from typing import List
import random, math

class Solution:

    def judgeSquareSum(self, c: int) -> bool:
        low = 0
        high = int(math.sqrt(c))
        while low <= high:
            res = low * low + high * high
            if res == c:
                return True
            elif res < c:
                low += 1
            else:
                high -= 1
        return False

import unittest

class TestSolution(unittest.TestCase):
    def testPickIndex(self):
        s = Solution([3,14,1,7])
        self.assertEqual(s.pickIndex(), 1)


if __name__ == '__main__':
    unittest.main()