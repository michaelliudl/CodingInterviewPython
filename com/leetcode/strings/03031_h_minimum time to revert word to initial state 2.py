from typing import List

class Solution:

    # Same as 3029, optimize with KMP
    def minimumTimeToInitialState1(self, word: str, k: int) -> int:
        n = len(word)
        dp = [0] * n
        v = 0
        for i in range(1, n):
            while v and word[i] != word[v]:
                v = dp[v - 1]
            dp[i] = v + (word[i] == word[v])
            v = dp[i]
        while v and (n - v) % k > 0:
            v = dp[v - 1]
        return (n - v + k - 1) // k

    # Optimize with z-function
    def minimumTimeToInitialState(self, word: str, k: int) -> int:

        def zFunc():
            z = [0] * n
            left = right = 0
            for i in range(1, n):
                if i < right:
                    z[i] = min(right - i, z[i - left])
                while (i + z[i]) < n and word[z[i]] == word[i + z[i]]:
                    z[i] += 1
                if i + z[i] > right:
                    left = i
                    right = i + z[i]
            return z

        n = len(word)
        res = 1
        maxOps = ((n - 1) // k) + 1
        z = zFunc()
        for res in range(1, maxOps):
            if z[res * k] >= (n - res * k):
                return res
        return maxOps

import unittest

class TestSolution(unittest.TestCase):
    def testMinimumTimeToInitialState(self):
        s = Solution()
        self.assertEqual(s.minimumTimeToInitialState(word = "abacaba", k = 3), 2)
        # self.assertEqual(s.minimumTimeToInitialState(word = "abacaba", k = 3), 2)


if __name__ == '__main__':
    unittest.main()