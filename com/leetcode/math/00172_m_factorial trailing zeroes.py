from typing import List

class Solution:

    # Count number of 10s in the factorial, which is then count of 5s in 1..n, since 2s are always more than 5s
    def trailingZeroes(self, n: int) -> int:
        result = 0
        while n >= 5:
            result += n // 5
            n //= 5
        return result


import unittest

class TestSolution(unittest.TestCase):
    def testTrailingZeroes(self):
        s = Solution()
        self.assertEqual(s.trailingZeroes(3), 0)
        self.assertEqual(s.trailingZeroes(5), 1)
        self.assertEqual(s.trailingZeroes(0), 0)
        self.assertEqual(s.trailingZeroes(10), 2)
        self.assertEqual(s.trailingZeroes(30), 7)


if __name__ == '__main__':
    unittest.main()