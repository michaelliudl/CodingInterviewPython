from typing import List

class Solution:

    # Sieve of Eratosthenes
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        arr = [i for i in range(n)]
        arr[1] = 0
        for i in range(n):
            cur = arr[i]
            if cur * cur > n:
                break
            if cur > 0:
                for j in range(i + cur, n, cur):
                    arr[j] = 0
        return sum(1 for a in arr if a > 0)


import unittest

class TestSolution(unittest.TestCase):
    def testbulbSwitch(self):
        s = Solution()
        self.assertEqual(s.bulbSwitch(3), 1)
        self.assertEqual(s.bulbSwitch(0), 0)
        self.assertEqual(s.bulbSwitch(1), 1)


if __name__ == '__main__':
    unittest.main()