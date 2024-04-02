from typing import List

class Solution:

    def countPalindromes(self, s: str) -> int:
        if not s or len(s) < 5:
            return 0
        MOD = 10 ** 9 + 7
        result = 0
        for a in range(10):
            for b in range(10):
                pattern = f'{a}{b}.{b}{a}'
                # dp[i] is number of subsequences of pattern[i..n) in s, pattern[2] can be any character
                dp = [0] * 6
                dp[-1] = 1
                for char in s:
                    for index, pat in enumerate(pattern):
                        if pat == '.' or pat == char:
                            dp[index] += dp[index + 1]
                result += dp[0]
                result %= MOD
        return result
            


import unittest

class TestSolution(unittest.TestCase):
    def testCountPalindromes(self):
        s = Solution()
        self.assertEqual(s.countPalindromes(s = "103301"), 2)
        self.assertEqual(s.countPalindromes(s = "0000000"), 21)
        self.assertEqual(s.countPalindromes(s = "9999900000"), 2)


if __name__ == '__main__':
    unittest.main()