from typing import List

class Solution:

    # Brute force by first prefix equals suffix
    # O(N**2)
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        res = 1
        for i in range(k, n, k):
            if word[i:] == word[:(n - i)]:
                break
            res += 1
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testMinimumTimeToInitialState(self):
        s = Solution()
        self.assertEqual(s.minimumTimeToInitialState(word = "abacaba", k = 3), 2)
        # self.assertEqual(s.minimumTimeToInitialState(word = "abacaba", k = 3), 2)


if __name__ == '__main__':
    unittest.main()