from typing import List
import math

class Solution:

    # Find min/max, if they are from same array, then find min/max from other arrays
    def maxDistance(self, arrays: List[List[int]]) -> int:
        maxVal = -math.inf
        minVal = math.inf
        maxIndex = minIndex = -1
        for index, array in enumerate(arrays):
            if array[-1] > maxVal:
                maxVal = array[-1]
                maxIndex = index
            if array[0] < minVal:
                minVal = array[0]
                minIndex = index
        if maxIndex != minIndex:
            return maxVal - minVal
        maxOther = -math.inf
        minOther = math.inf
        for index, array in enumerate(arrays):
            if index != maxIndex and array[-1] > maxOther:
                maxOther = array[-1]
            if index != minIndex and array[0] < minOther:
                minOther = array[0]
        return max((maxVal - minOther), (maxOther - minVal))
    
import unittest

class TestSolution(unittest.TestCase):
    def testMaxDistance(self):
        s = Solution()
        self.assertEqual(s.maxDistance(arrays = [[1,2,3],[4,5],[1,2,3]]), 4)
        self.assertEqual(s.maxDistance(arrays = [[1],[1]]), 0)
        self.assertEqual(s.maxDistance(arrays = [[1,4],[0,5]]), 4)

if __name__ == '__main__':
    unittest.main()