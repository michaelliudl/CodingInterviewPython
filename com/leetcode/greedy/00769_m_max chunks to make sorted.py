from typing import List
import math

class Solution:

    # Greedily check if current number is at the correct position
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res = 0
        expectedNum = -math.inf
        for i, num in enumerate(arr):
            expectedNum = max(expectedNum, num)
            if expectedNum == i:
                res += 1
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testMaxSlidingWindow(self):
        s = Solution()
        self.assertEqual(s.maxSlidingWindowMonoToneQueue1([1,3,-1,-3,5,3,6,7],3), [3,3,5,5,6,7])
        self.assertEqual(s.maxSlidingWindowMonoToneQueue1([1],1), [1])



if __name__ == '__main__':
    unittest.main()