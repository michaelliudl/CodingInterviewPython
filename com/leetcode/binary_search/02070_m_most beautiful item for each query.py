from typing import List
import bisect

class Solution:

    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        n = len(items)
        criteria, scores = [0] * n, [0] * n
        for index, [crit, score] in enumerate(items):
            criteria[index] = crit
            scores[index] = score

        maxScores = [0] * (n + 1)
        for index, score in enumerate(scores):
            maxScores[index + 1] = max(maxScores[index], score)
        
        return [maxScores[bisect.bisect_right(criteria, query)] for query in queries]


import unittest

class TestSolution(unittest.TestCase):
    def testSearch(self):
        s = Solution()
        self.assertEqual(s.search([1], 1), 0)
        self.assertEqual(s.search([4,5,6,7,0,1,2], 0), 4)



if __name__ == '__main__':
    unittest.main()