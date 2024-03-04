from typing import List


class Solution:

    # Brute, use bit mask instead of set to reduce to O(n**2)
    def maxProduct(self, words: List[str]) -> int:

        def mask(word):
            result = 0
            for ch in word:
                result |= (1 << (ord(ch) - ord('a')))
            return result

        if not words:
            return 0
        maskAndLen = [None] * len(words)
        for index, word in enumerate(words):
            wordMask = mask(word)
            maskAndLen[index] = (wordMask, len(word))
        maxProd = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                maskI, lenI = maskAndLen[i]
                maskJ, lenJ = maskAndLen[j]
                if maskI & maskJ == 0:
                    maxProd = max(maxProd, lenI * lenJ)
        return maxProd

import unittest

class TestSolution(unittest.TestCase):
    def testFindRedundantConnection(self):
        s = Solution()
        self.assertEqual(s.findRedundantConnection(edges = [[1,2],[1,3],[2,3]]), [2,3])
        self.assertEqual(s.findRedundantConnection(edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]), [1,4])
        # self.assertEqual(s.findRedundantConnection([0,0,0]), [[0,0,0]])


if __name__ == '__main__':
    unittest.main()