from typing import List

class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:

        def op(wordList):
            prefix = wordList[:k + 1]
            suffix = wordList[(k * (len(word) % k) - 1):]
            commonLen = 0
            while commonLen < min(len(prefix), len(suffix)):
                if prefix[commonLen] == suffix[commonLen]:
                    commonLen += 1
                else:
                    break
            toAdd = wordList[commonLen:commonLen + k]
            wordList = wordList[k:]
            wordList.extend(toAdd)
            return wordList

        if not word or k <= 0:
            return 0
        original = list(word)
        wordList = list(word)
        result = 1
        wordList = op(wordList)
        while wordList != original:
            wordList = op(wordList)
            result += 1
        return result

import unittest

class TestSolution(unittest.TestCase):
    def testMinimumTimeToInitialState(self):
        s = Solution()
        self.assertEqual(s.minimumTimeToInitialState(word = "abacaba", k = 3), 2)
        # self.assertEqual(s.minimumTimeToInitialState(word = "abacaba", k = 3), 2)


if __name__ == '__main__':
    unittest.main()