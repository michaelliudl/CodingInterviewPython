from typing import Deque

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if not word and not abbr:
            return True
        if (not word and abbr) or (word and not abbr):
            return False
        wordIndex = abbrIndex = 0
        numStart = -1
        while wordIndex < len(word) and abbrIndex < len(abbr):
            if '0' <= abbr[abbrIndex] <= '9':
                if numStart < 0:
                    numStart = abbrIndex
                if abbr[numStart] == '0':
                    return False
                abbrIndex += 1
            elif numStart >= 0:
                num = int(abbr[numStart:abbrIndex])
                numStart = -1
                if wordIndex + num > len(word):
                    return False
                wordIndex += num
            else:
                if word[wordIndex] != abbr[abbrIndex]:
                    return False
                wordIndex += 1
                abbrIndex += 1
        if wordIndex == len(word) and abbrIndex == len(abbr):
            return True
        if wordIndex < len(word) and numStart >= 0:
            num = int(abbr[numStart:])
            if wordIndex + num == len(word):
                return True
        return False
    
import unittest

class TestSolution(unittest.TestCase):
    def testValidWordAbbreviation(self):
        s = Solution()
        self.assertEqual(s.validWordAbbreviation(word = "internationalization", abbr = "i5a11o1"), True)
        self.assertEqual(s.validWordAbbreviation(word = "internationalization", abbr = "i12iz4n"), True)
        self.assertEqual(s.validWordAbbreviation(word = "apple", abbr = "a2e"), False)


if __name__ == '__main__':
    unittest.main()
