from typing import List
import re, math

class Solution:

    def fractionAddition(self, expression: str) -> str:
        nums = list(map(int, re.findall('[+-]?[0-9]+', expression)))
        numerator = 0
        denominator = 1
        for curNume, curDenom in zip(nums[::2], nums[1::2]):
            numerator = numerator * curDenom + denominator * curNume
            denominator *= curDenom
            gcd = math.gcd(numerator, denominator)
            numerator //= gcd
            denominator //= gcd
        return str(numerator) + '/' + str(denominator)

import unittest

class TestSolution(unittest.TestCase):
    def testRotate(self):
        s = Solution()
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        s.rotate(matrix)
        self.assertEqual(matrix, [[7,4,1],[8,5,2],[9,6,3]])
        matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        s.rotate(matrix)
        self.assertEqual(matrix, [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])

if __name__ == '__main__':
    unittest.main()