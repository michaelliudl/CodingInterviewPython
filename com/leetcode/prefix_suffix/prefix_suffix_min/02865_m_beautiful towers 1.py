from typing import List
import math

class Solution:
    # Brute force for small constraint `3 <= nums.length <= 10 ** 3` O(n**2)
    # Find largest possible height before and after current index by comparing prev/after height chosen and maxHeight allowance
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        if not maxHeights:
            return 0
        result = 0
        n = len(maxHeights)
        for i, mh in enumerate(maxHeights):
            towers = [0] * n
            towers[i] = mh
            for j in range(i - 1, -1, -1):
                towers[j] = min(towers[j + 1], maxHeights[j])
            for j in range(i + 1, n):
                towers[j] = min(towers[j - 1], maxHeights[j])
            result = max(result, sum(towers))
        return result

import unittest

class TestSolution(unittest.TestCase):
    def testNumMatrix(self):
        nm = NumMatrix(matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
        self.assertEqual(nm.sumRegion(2, 1, 4, 3), 8)
        self.assertEqual(nm.sumRegion(1, 1, 2, 2), 11)
        self.assertEqual(nm.sumRegion(1, 2, 2, 4), 12)


if __name__ == '__main__':
    unittest.main()