from typing import List
import math, functools

class Solution:

    # DP top-down, recursion with memoization
    def stoneGameII(self, piles: List[int]) -> int:
        
        @functools.cache
        def dp(actor, index, M):
            if index == len(piles):
                return 0
            res = 0 if actor == 'A' else math.inf   # Result should be maximized for 'Alice' and minimized for 'Bob'
            total = 0
            for X in range(1, 2 * M + 1):
                if index + X > len(piles):
                    break
                total += piles[index + X - 1]
                nextRes = dp(actor='B' if actor == 'A' else 'A', index=(index + X), M=max(M, X))
                if actor == 'A':
                    res = max(res, total + nextRes)
                else:
                    res = min(res, nextRes)
            return res
        return dp(actor='A', index=0, M=1)


import unittest

class TestSolution(unittest.TestCase):
    def testStoneGameII(self):
        s = Solution()
        self.assertEqual(s.stoneGameII(piles = [2,7,9,4,4]), 10)
        self.assertEqual(s.stoneGameII(piles = [1,2,3,4,5,100]), 104)
        


if __name__ == '__main__':
    unittest.main()