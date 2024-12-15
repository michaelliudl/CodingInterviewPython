from typing import List, DefaultDict, Counter

class Solution:

    def takeCharacters(self, s: str, k: int) -> int:
        counts = Counter(s)
        for char in 'abc':
            if counts[char] < k:    # Not enough chars
                return -1
        res = n = len(s)
        left = 0
        for i, char in enumerate(s):
            counts[char] -= 1
            while counts[char] < k:
                counts[s[left]] += 1
                left += 1
            res = min(res, n - (i - left + 1))
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testminWindow(self):
        s = Solution()
        self.assertEqual(s.minWindow(s = "ADOBECODEBANC", t = "ABC"), "BANC")
        self.assertEqual(s.minWindow(s = "a", t = "a"), 'a')
        self.assertEqual(s.minWindow(s = "a", t = "aa"), '')


if __name__ == '__main__':
    unittest.main()