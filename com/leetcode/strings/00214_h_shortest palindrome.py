from typing import List

class Solution:

    # Brute force to find longest prefix in reversed string
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        for i in range(len(rev)):
            if s.startswith(rev[i:]):
                return rev[:i] + s
        return rev + s


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