from typing import List
import math

class Solution:

    # DFS with memoization
    def findRotateSteps(self, ring: str, key: str) -> int:
        # DFS with position in both strings
        def dfs(posInRing, posInKey):
            if posInKey == len(key):
                return 0
            if (posInRing, posInKey) in cache:
                return cache[(posInRing, posInKey)]
            steps = math.inf
            for nextPos in range(len(ring)):            # Try all chars in `ring` that matches current char in `key`
                if ring[nextPos] == key[posInKey]:
                    diff = abs(posInRing - nextPos)
                    turns = min(diff, len(ring) - diff) # Choose less turns between clockwise and counter-clockwise
                    nextSteps = dfs(nextPos, posInKey + 1)  # DFS to get min steps to end from next position in `ring` and `key`
                    steps = min(steps, (turns + 1 + nextSteps)) # Current min steps including turns, press and min steps from next position
            cache[(posInRing, posInKey)] = steps
            return steps

        cache = {}
        return dfs(posInRing = 0, posInKey = 0)

    # Greedy will work if `ring` has unique characters. With duplicates, need to use DP to find optimal result among choices.

    # DP bottom up
    # dp = len(key) rows, len(ring) columns
    # Fill dp bottom up, optimized to 1D dp array since next row only depends on current row
    def findRotateStepsDPBU(self, ring: str, key: str) -> int:
        dp = [0] * len(ring)
        for k in range(len(key) - 1, -1, -1):
            nextDP = [math.inf] * len(ring)
            for r in range(len(ring)):
                for i, char in enumerate(ring):
                    if char == key[k]:
                        minDiff = min(abs(r - i), len(ring) - abs(r - i))
                        nextDP[r] = min(nextDP[r], minDiff + 1 + dp[i])
            dp = nextDP
        return dp[0]

import unittest

class TestSolution(unittest.TestCase):
    def testLargestDivisibleSubset(self):
        s = Solution()
        self.assertEqual(s.largestDivisibleSubset(nums = [1,2,3]), [2,1])
        self.assertEqual(s.largestDivisibleSubset(nums = [1,2,4,8]), [8,4,2,1])
        


if __name__ == '__main__':
    unittest.main()