from typing import List, Counter

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)

import unittest

class TestSolution(unittest.TestCase):
    def testWordPattern(self):
        s = Solution()
        self.assertEqual(s.wordPattern(pattern = "abc", s = "b c a"), True)
        self.assertEqual(s.wordPattern(pattern = "abba", s = "dog dog dog dog"), False)
        self.assertEqual(s.wordPattern(pattern = "abba", s = "dog cat cat dog"), True)
        self.assertEqual(s.wordPattern(pattern = "abba", s = "dog cat cat fish"), False)
        self.assertEqual(s.wordPattern(pattern = "aaaa", s = "dog cat cat dog"), False)
        


if __name__ == '__main__':
    unittest.main()