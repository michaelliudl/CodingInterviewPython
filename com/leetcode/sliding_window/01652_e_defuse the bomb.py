from typing import List

class Solution:

    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        res = [0] * n
        if k == 0:
            return res

        start = 1 if k > 0 else n + k
        end = k if k > 0 else n - 1
        winSum = 0
        for i in range(start, end + 1):
            winSum += code[i]
        for i in range(n):
            res[i] = winSum
            winSum -= code[start % n]
            start += 1
            end += 1
            winSum += code[end % n]
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testMaximumLengthSubstring(self):
        s = Solution()
        self.assertEqual(s.maximumLengthSubstring(s = "bcbbbcba"), 4)
        self.assertEqual(s.maximumLengthSubstring(s = "aaaa"), 2)


if __name__ == '__main__':
    unittest.main()