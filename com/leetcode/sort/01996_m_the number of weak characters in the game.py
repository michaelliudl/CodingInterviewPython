from typing import List
import heapq
import random

class Solution:
    
    # Sort by first property desc and second property asc
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda prop: (-prop[0], prop[1]))
        maxDef = 0
        result = 0
        for _, defen in properties:
            if defen < maxDef:              # Valid if second property is less than max, since first property is already descending
                result += 1
            maxDef = max(maxDef, defen)     # Update and track max value of second property
        return result

import unittest

class TestSolution(unittest.TestCase):
    def testSortArray(self):
        s = Solution()
        self.assertEqual(s.sortArray(nums = [5,2,3,1]), [1,2,3,5])
        self.assertEqual(s.sortArray(nums = [5,1,1,2,0,0]), [0,0,1,1,2,5])


if __name__ == '__main__':
    unittest.main()