from typing import List

class Solution:

    def distinctSubseqII(self, s: str) -> int:
        if not s:
            return 0
        MOD = 10 ** 9 + 7
        # endsIn[i] is the number of distinct subsequences that ends in each lower case characters chr(i + ord('a'))
        endsIn = [0] * 26
        for char in s:
            endsIn[ord(char) - ord('a')] = (sum(endsIn) + 1) % MOD
        return sum(endsIn) % MOD


import unittest

class TestSolution(unittest.TestCase):
    def testDistinctSubseqII(self):
        s = Solution()
        self.assertEqual(s.distinctSubseqII(s = "abc"), 7)
        self.assertEqual(s.distinctSubseqII(s = "aba"), 6)
        self.assertEqual(s.distinctSubseqII(s = "aaa"), 3)


if __name__ == '__main__':
    unittest.main()