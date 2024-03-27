from typing import Deque

'''
A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.
'''

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
