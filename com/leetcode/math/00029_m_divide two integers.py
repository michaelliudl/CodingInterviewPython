from typing import List

class Solution:

    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            raise ValueError('divisor is zero')
        if dividend == 0:
            return 0
        isResultPositive = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)
        dvd = abs(dividend)
        dvs = abs(divisor)
        result = 0
        while dvd >= dvs:
            temp = dvs
            i = 0
            while dvd >= temp:
                dvd -= temp
                result += 1 << i
                i += 1
                temp <<= 1
        if not isResultPositive:
            result = -result
        if result > 2 ** 31 -1:
            result = 2 ** 31 - 1
        if result < -(2 ** 31):
            result = -(2 ** 31)
        return result
        

import unittest

class TestSolution(unittest.TestCase):
    def testDivide(self):
        s = Solution()
        self.assertEqual(s.divide(dividend = 10, divisor = 3), 3)
        self.assertEqual(s.divide(dividend = 7, divisor = -3), -2)
        self.assertEqual(s.divide(dividend = 1, divisor = 1), 1)


if __name__ == '__main__':
    unittest.main()