from typing import List

class Solution:

    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if len(sentence1) == len(sentence2):
            return sentence1 == sentence2
        words1 = sentence1.split()
        words2 = sentence2.split()
        wordsLen1 = len(words1)
        wordsLen2 = len(words2)
        if wordsLen1 > wordsLen2:
            return self.areSentencesSimilar(sentence2, sentence1)
        diff = wordsLen2 - wordsLen1
        i = 0
        while i < wordsLen1 and words1[i] == words2[i]:     # Move over same leading words
            i += 1
        while i < wordsLen1 and words1[i] == words2[i + diff]:  # Should be same words after `diff` number of words
            i += 1
        return i == wordsLen1   # Should cover the whole shorter sentence



import unittest

class TestSolution(unittest.TestCase):
    def testMaxArea(self):
        s = Solution()
        self.assertEqual(s.maxArea(height = [1,8,6,2,5,4,8,3,7]), 49)
        self.assertEqual(s.maxArea(height = [1,1]), 1)


if __name__ == '__main__':
    unittest.main()