from typing import List
import math, bisect

class Solution:

    def primeSubOperation(self, nums: list[int]) -> bool:

        # Sieve of Eratosthenes
        def findPrimes(bound):
            isPrime = [True] * bound
            isPrime[0] = isPrime[1] = False
            for i in range(2, int(math.sqrt(bound)) + 1):
                if isPrime[i]:
                    for j in range(i * i, bound, i):
                        isPrime[j] = False
            return [i for i in range(bound) if isPrime[i]]

        upperBound = 1000
        primes = findPrimes(upperBound)
        prev = 0
        for num in nums:
            index = bisect.bisect_left(primes, num - prev)
            if index > 0:
                num -= primes[index - 1]
            if num <= prev:
                return False
            prev = num
        return True

import unittest

class TestSolution(unittest.TestCase):
    def testSearchMatrix(self):
        s = Solution()
        self.assertEqual(s.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3), True)
        self.assertEqual(s.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13), False)


if __name__ == '__main__':
    unittest.main()