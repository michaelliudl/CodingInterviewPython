from typing import List

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        if not wordsDict or len(wordsDict) < 2 or word1 == word2:
            return 0
        wordsMap = {}
        for index, word in enumerate(wordsDict):
            if word not in wordsMap:
                wordsMap[word] = []
            wordsMap[word].append(index)
        result = len(wordsDict)
        for index1 in wordsMap[word1]:
            for index2 in wordsMap[word2]:
                result = min(result, abs(index1 - index2))
        return result
    
import unittest

class TestSolution(unittest.TestCase):
    def testFindMissingRanges(self):
        s = Solution()
        self.assertEqual(s.shortestDistance(wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"), 3)
        self.assertEqual(s.shortestDistance(wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"), 1)


if __name__ == '__main__':
    unittest.main()
