from typing import List

class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        div = x
        sumDigits = 0
        while div > 0:
            sumDigits += div % 10
            div //= 10
        return sumDigits if x % sumDigits == 0 else -1

import unittest

class TestSolution(unittest.TestCase):
    def testThreeSum(self):
        s = Solution()
        self.assertEqual(s.threeSum([-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]])
        self.assertEqual(s.threeSum([0,1,1]), [])
        self.assertEqual(s.threeSum([0,0,0]), [[0,0,0]])


if __name__ == '__main__':
    unittest.main()