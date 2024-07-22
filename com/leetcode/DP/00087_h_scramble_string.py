from typing import List, Counter
import functools

class Solution:

    # DP top-down with memoization
    def isScramble(self, s1: str, s2: str) -> bool:
        
        @functools.cache
        def dp(s1, s2):
            if s1 == s2:
                return True
            for i in range(1, len(s1)):
                if dp(s1[:i], s2[:i]) and dp(s1[i:], s2[i:]):
                    return True
                if dp(s1[:i], s2[-i:]) and dp(s1[i:], s2[:-i]):
                    return True
            return False

        return dp(s1, s2)


import unittest

class TestSolution(unittest.TestCase):
    def testIsScramble(self):
        s = Solution()
        self.assertEqual(s.isScramble(s1 = "great", s2 = "rgeat"), True)
        self.assertEqual(s.isScramble(s1 = "abcde", s2 = "caebd"), False)
        self.assertEqual(s.isScramble(s1 = "a", s2 = "a"), True)
        


if __name__ == '__main__':
    unittest.main()