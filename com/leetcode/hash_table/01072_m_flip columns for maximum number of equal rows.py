from typing import List, DefaultDict

class Solution:

    # Convert rows to continuous '*'s when elements are same and add a '|' when element change.
    # Answer is the most frequency of patterns
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        patterns = DefaultDict(int)
        for row in matrix:
            pattern = ['*']
            for i in range(1, len(row)):
                if row[i] != row[i - 1]:
                    pattern.append('|')
                pattern.append('*')
            patterns[''.join(pattern)] += 1
        return max(patterns.values())

import unittest

class TestSolution(unittest.TestCase):
    def testMaxEqualRowsAfterFlips(self):
        s = Solution()
        self.assertEqual(s.maxEqualRowsAfterFlips(matrix = [[0,1],[1,1]]), 1)
        self.assertEqual(s.maxEqualRowsAfterFlips(matrix = [[0,1],[1,0]]), 2)
        self.assertEqual(s.maxEqualRowsAfterFlips(matrix = [[0,0,0],[0,0,1],[1,1,0]]), 2)
        self.assertEqual(s.maxEqualRowsAfterFlips(matrix = [[1,0,0,0,1,1,1,0,1,1,1],[1,0,0,0,1,0,0,0,1,0,0],[1,0,0,0,1,1,1,0,1,1,1],[1,0,0,0,1,0,0,0,1,0,0],[1,1,1,0,1,1,1,0,1,1,1]]), 2)


if __name__ == '__main__':
    unittest.main()