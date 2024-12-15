from typing import List, DefaultDict, Counter
import heapq

class Solution:

    # Greedily accumulate sum and number of integers counted
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        totalSum = res = 0
        banSet = set(banned)
        for num in range(1, n + 1):
            if num not in banSet and totalSum + num <= maxSum:
                totalSum += num
                res += 1
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testMinOperations(self):
        s = Solution()
        self.assertEqual(s.minOperations(k = 11), 5)
        self.assertEqual(s.minOperations(k = 1), 0)


if __name__ == '__main__':
    unittest.main()