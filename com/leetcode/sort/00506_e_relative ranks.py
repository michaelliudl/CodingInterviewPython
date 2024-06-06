from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        scores = [(s, i) for i, s in enumerate(score)]
        scores.sort(reverse=True)
        res = [''] * len(score)
        for i, s in enumerate(scores):
            _, index = s
            if i == 0:
                res[index] = 'Gold Medal'
            elif i == 1:
                res[index] = 'Silver Medal'
            elif i == 2:
                res[index] = 'Bronze Medal'
            else:
                res[index] = str(i + 1)
        return res

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def testSortColors(self):
        input = [2,0,2,1,1,0]
        expected = [0,0,1,1,2,2]
        self.s.sortColors(input)
        self.assertEqual(input, expected)

if __name__ == '__main__':
    unittest.main()