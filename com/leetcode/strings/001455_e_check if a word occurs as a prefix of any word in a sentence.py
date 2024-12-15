from typing import List

class Solution:

    # Simulate
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, word in enumerate(sentence.split()):
            if word.startswith(searchWord):
                return i + 1
        return -1


import unittest

class TestSolution(unittest.TestCase):
    def testIsAlienSorted(self):
        s = Solution()
        self.assertEqual(s.isAlienSorted(words = ["hello","hello"], order = "abcdefghijklmnopqrstuvwxyz"), True)
        self.assertEqual(s.isAlienSorted(words = ["hello","hellob","helloa"], order = "hlabcdefgijkmnopqrstuvwxyz"), False)
        self.assertEqual(s.isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"), True)
        self.assertEqual(s.isAlienSorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"), False)
        self.assertEqual(s.isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"), False)
        

if __name__ == '__main__':
    unittest.main()