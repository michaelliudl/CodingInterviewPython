from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counts = Counter(arr1)
        res = []
        for elem in arr2:
            for _ in range(counts[elem]):
                res.append(elem)
            del counts[elem]
        for elem in sorted(counts.keys()):
            for _ in range(counts[elem]):
                res.append(elem)
        return res

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