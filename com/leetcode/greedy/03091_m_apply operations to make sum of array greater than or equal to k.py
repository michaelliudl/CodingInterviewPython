from typing import List

class Solution:

    # Greedy, increment then duplicate
    def minOperations(self, k: int) -> int:
        if k <= 1:
            return 0
        result = float('inf')
        for i in range(1, k // 2 + 2):
            ops = (i - 1) + ((k // i - 1) if k % i == 0 else (k // i))
            result = min(result, ops)
        return result


import unittest

class TestSolution(unittest.TestCase):
    def testMinOperations(self):
        s = Solution()
        self.assertEqual(s.minOperations(k = 11), 5)
        self.assertEqual(s.minOperations(k = 1), 0)


if __name__ == '__main__':
    unittest.main()