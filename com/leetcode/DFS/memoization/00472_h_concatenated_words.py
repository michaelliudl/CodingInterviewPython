from typing import List

class Solution:

    # Backtrack with memoization
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        def isConcat(word):
            if word in mem:
                return mem[word]
            flag = False
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in wordSet and (suffix in wordSet or isConcat(suffix)):
                    flag = True
                    break
            mem[word] = flag
            return flag

        if not words:
            return []
        wordSet = set()
        for word in words:
            wordSet.add(word)
        mem = {}
        minLen = min([len(word) for word in words])
        result = []
        for word in words:
            if len(word) > minLen and isConcat(word):
                result.append(word)
        return result

import unittest

class TestSolution(unittest.TestCase):
    def testFindAllConcatenatedWordsInADict(self):
        s = Solution()
        self.assertEqual(s.findAllConcatenatedWordsInADict(words = ["a","b","ab","abc"]), ["ab"])
        self.assertEqual(s.findAllConcatenatedWordsInADict(words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]),
                         ["catsdogcats","dogcatsdog","ratcatdogcat"])
        self.assertEqual(s.findAllConcatenatedWordsInADict(words = ["cat","dog","catdog"]), ["catdog"])
        


if __name__ == '__main__':
    unittest.main()