from typing import List
import math

class Solution:

    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'
        midIndex = math.pow(2, n - 1)   # Middle index of '1'
        if k == midIndex:
            return '1'
        if k < midIndex:
            return self.findKthBit(n - 1, k)
        return '1' if self.findKthBit(n - 1, midIndex * 2 - k) == '0' else '0'

    # Simulate
    def findKthBitBrute(self, n: int, k: int) -> str:

        def form(i):
            if i == 1:
                return '0'
            prev = form(i - 1)
            prevList = ['1' if prevChar == '0' else '0' for prevChar in prev]
            prevList.reverse()
            return prev + '1' + ''.join(prevList)

        return form(n)[k - 1]


import unittest

class TestSolution(unittest.TestCase):
    def testMyAtoi(self):
        s = Solution()
        self.assertEqual(s.myAtoi(s = "   +0 123"), 0)
        self.assertEqual(s.myAtoi(s = "00000-42a1234"), 0)
        self.assertEqual(s.myAtoi(s = "   -42"), -42)
        self.assertEqual(s.myAtoi(s = "42"), 42)
        self.assertEqual(s.myAtoi(s = "+-12"), 0)
        self.assertEqual(s.myAtoi(s = "words and 987"), 0)
        self.assertEqual(s.myAtoi(s = "4193 with words"), 4193)
        

if __name__ == '__main__':
    unittest.main()