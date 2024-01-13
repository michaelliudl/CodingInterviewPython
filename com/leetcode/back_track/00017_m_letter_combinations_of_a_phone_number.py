from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d={'2':'abc', '3':'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 
           'tuv', '9': 'wxyz'}
        r,path=[],[]
        self.backtrack(digits, 0, d, r, path)
        return r

    def backtrack(self, digits, startIndex, d, r, path):
        if len(path)==len(digits):
            r.append(''.join(path))
            return

        for i in range(startIndex, len(digits)):
            num=digits[i]
            if num in d:
                for c in d[num]:
                    path.append(c)
                    self.backtrack(digits, i+1, d, r, path)
                    path.pop()
        

import unittest

class TestSolution(unittest.TestCase):
    def testLetterCombinations(self):
        s = Solution()
        self.assertEqual(s.letterCombinations("23"), ["ad","ae","af","bd","be","bf","cd","ce","cf"])
        self.assertEqual(s.letterCombinations("2"), ["a","b","c"])
        self.assertEqual(s.letterCombinations(""), [])


if __name__ == '__main__':
    unittest.main()