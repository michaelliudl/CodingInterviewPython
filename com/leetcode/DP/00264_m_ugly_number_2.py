from typing import List
import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 1: return n
        ugly = [1]*n
        prod2,prod3,prod5 = 0,0,0
        for i in range(1,n):
            nextUgly = min(ugly[prod2]*2, ugly[prod3]*3, ugly[prod5]*5)
            ugly[i] = nextUgly
            if nextUgly == ugly[prod2]*2:
                prod2 += 1
            if nextUgly == ugly[prod3]*3:
                prod3 += 1
            if nextUgly == ugly[prod5]*5:
                prod5 += 1
        return ugly[-1]

import unittest

class TestSolution(unittest.TestCase):
    def testNthUglyNumber(self):
        s = Solution()
        self.assertEqual(s.nthUglyNumber(n = 10), 12)
        self.assertEqual(s.nthUglyNumber(n = 1), 1)



if __name__ == '__main__':
    unittest.main()