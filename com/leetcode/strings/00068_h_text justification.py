from typing import List

class Solution:

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        if not words or maxWidth <= 0:
            return words
        result = []
        row = []
        curLen = 0
        for i in range(len(words)):
            word = words[i]
            if curLen + len(word) > maxWidth:
                textLen = curLen - len(row)
                totalSpaces = maxWidth - textLen
                remSpaces = totalSpaces % (len(row) - 1) if len(row) > 1 else 0
                spaces = totalSpaces // (len(row) - 1) if len(row) > 1 else totalSpaces
                rowWord = ''
                for j in range(len(row)):
                    rowWord += row[j]
                    if len(row) == 1 or j < len(row) - 1:
                        rowWord += ' ' * (spaces + (1 if remSpaces > 0 else 0))
                        if remSpaces > 0:
                            remSpaces -= 1
                result.append(rowWord)
                row = [word]
                curLen = len(word) + 1
            else:
                row.append(word)
                curLen += (len(word) + 1)
        if row:
            lastRow = ' '.join(row)
            lastRow += ' ' * (maxWidth - len(lastRow))
            result.append(lastRow)
        return result


import unittest

class TestSolution(unittest.TestCase):
    def testFullJustify(self):
        s = Solution()
        self.assertEqual(s.fullJustify(words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16), 
                         [
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
])
        self.assertEqual(s.fullJustify(words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16), 
                         [
   "This    is    an",
   "example  of text",
   "justification.  "
])
        self.assertEqual(s.fullJustify(words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20),
                         [
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
])

if __name__ == '__main__':
    unittest.main()