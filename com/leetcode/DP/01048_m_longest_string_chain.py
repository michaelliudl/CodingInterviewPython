from typing import List

class Solution:

    # Sort by length and DP
    def longestStrChain(self, words: List[str]) -> int:

        def chain(short, long):
            for i in range(len(long)):
                if (long[:i] + long[i+1:]) == short:
                    return True
            return False

        if not words:
            return 0
        words.sort(key = lambda word: (len(word), word))
        dp = [1] * len(words)
        for i in range(1, len(words)):
            wordI = words[i]
            for j in range(i-1, -1, -1):
                wordJ = words[j]
                if len(wordJ) == len(wordI) - 1:
                    if chain(wordJ, wordI):
                        dp[i] = max(dp[i], dp[j] + 1)
                if len(wordJ) < len(wordI) - 1:
                    break
        return max(dp)


import unittest

class TestSolution(unittest.TestCase):
    def testLongestStrChain(self):
        s = Solution()
        self.assertEqual(s.longestStrChain(words = ["a","b","ba","bca","bda","bdca"]), 4)
        self.assertEqual(s.longestStrChain(words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]), 5)
        self.assertEqual(s.longestStrChain(words = ["abcd","dbqca"]), 1)
        


if __name__ == '__main__':
    unittest.main()