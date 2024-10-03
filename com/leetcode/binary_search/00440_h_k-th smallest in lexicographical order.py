from typing import List

class Solution:

    # Binary search in a 10-ary tree
    def findKthNumber(self, n: int, k: int) -> int:

        def findGap(cur):
            gap = 0
            neighbor = cur + 1
            while cur <= n:
                gap += min(neighbor, n + 1) - cur
                cur *= 10
                neighbor *= 10
            return gap

        res = 1
        step = 1
        while step < k:
            gap = findGap(res)
            if step + gap <= k:
                res += 1
                step += gap     # Move right inside current subtree
            else:
                res *= 10
                step += 1       # Move one level in the tree
        return res

    # TLE, Case 40
    def findKthNumberGenerate(self, n: int, k: int) -> int:
        res = 1
        i = 1
        while i < k:
            if res * 10 <= n:
                res *= 10
            else:
                while res % 10 == 9 or res == n:
                    res //= 10
                res += 1
            i += 1
        return res

    # MLE, Case 32
    def findKthNumberBrute(self, n: int, k: int) -> int:
        return [int(s) for s in (list(sorted([str(num) for num in range(1, n + 1)])))][k - 1]

import unittest

class TestSolution(unittest.TestCase):

    def testFindKthNumber(self):
        s = Solution()
        self.assertEqual(s.findKthNumber(n = 13, k = 2), 10)
        self.assertEqual(s.findKthNumber(n = 1, k = 1), 1)
        self.assertEqual(s.findKthNumber(n = 9885387, k = 8786251), 8907623)      # Case 32
        self.assertEqual(s.findKthNumber(n = 681692778, k = 351251360), 416126219)  # Case 40

if __name__ == '__main__':
    unittest.main()