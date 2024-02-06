from typing import List

class Solution:

    # dp[i][j] is True if can make a size j jump to stone i
    def canCross(self, stones: List[int]) -> bool:
        if not stones: return True
        n = len(stones)
        dp=[[False] * (n+1) for _ in range(n)]
        dp[0][0] = True
        for i in range(1, n):
            for j in range(i):
                gap = stones[i] - stones[j]
                if gap > n: continue
                for jump in (gap-1, gap, gap+1):
                    if jump >= 0 and jump <= n:
                        dp[i][gap] |= dp[j][jump]
        for result in dp[n-1]:
            if result: return True
        return False

import unittest

class TestSolution(unittest.TestCase):
    def testFindItinerary(self):
        s = Solution()
        self.assertEqual(s.canCross(stones = [0,1,3,5,6,8,12,17]), True)
        self.assertEqual(s.canCross(stones = [0,1,2,3,4,8,9,11]), False)

if __name__ == '__main__':
    unittest.main()