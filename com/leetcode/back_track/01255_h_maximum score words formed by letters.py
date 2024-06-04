from typing import List, Counter

class Solution:

    # Backtrack and try to for each words from currently available letters
    def maxScoreWords(self, words: List[str], letters: List[chr], score: List[int]) -> int:

        def canFormWord(word):
            letterCountForWord = Counter(word)
            for char, count in letterCountForWord.items():
                if count > letterCount[char]:
                    return False
            return True

        def getScore(word):
            return sum(score[ord(char) - ord('a')] for char in word)

        def backtrack(index):
            if index == len(words):
                return 0
            score = backtrack(index + 1)    # Skip word at `index`
            if canFormWord(words[index]):
                for char in words[index]:
                    letterCount[char] -= 1
                score = max(score, getScore(words[index]) + backtrack(index + 1))
                for char in words[index]:
                    letterCount[char] += 1
            return score
        
        letterCount = Counter(letters)
        return backtrack(0)

import unittest

class TestSolution(unittest.TestCase):
    def testMaxLength(self):
        s = Solution()
        self.assertEqual(s.maxLength(arr = ["un","iq","ue"]), 4)
        self.assertEqual(s.maxLength(arr = ["cha","r","act","ers"]), 6)
        self.assertEqual(s.maxLength(arr = ["abcdefghijklmnopqrstuvwxyz"]), 26)
        


if __name__ == '__main__':
    unittest.main()