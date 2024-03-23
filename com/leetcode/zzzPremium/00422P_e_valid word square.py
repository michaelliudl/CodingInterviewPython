from typing import List

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        if not words:
            return False
        prefixWords = []
        maxLen = max(len(word) for word in words)
        for col in range(maxLen):
            prefix = []
            for word in words:
                if col < len(word):
                    prefix.append(word[col])
            prefixWords.append(''.join(prefix))
        return prefixWords == words
    
import unittest

class TestSolution(unittest.TestCase):
    def testValidWordSquare(self):
        s = Solution()
        self.assertEqual(s.validWordSquare(words = ["abcd","bnrt","crmy","dtye"]), True)
        self.assertEqual(s.validWordSquare(words = ["abcd","bnrt","crm","dt"]), True)
        self.assertEqual(s.validWordSquare(words = ["ball","area","read","lady"]), False)


if __name__ == '__main__':
    unittest.main()
