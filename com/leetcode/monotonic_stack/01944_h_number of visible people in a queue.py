from typing import List
import heapq

class Solution:

    # Mono large stack holding index
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        if not heights:
            return heights
        stack = [0]
        result = [0] * len(heights)
        for i in range(1, len(heights)):
            while stack and (heights[i] >= heights[stack[-1]]):
                result[stack[-1]] += 1
                stack.pop()
            if stack:
                result[stack[-1]] += 1
            stack.append(i)
        return result

import unittest

class TestSolution(unittest.TestCase):
    def testSumSubarrayMins(self):
        s = Solution()
        self.assertEqual(s.sumSubarrayMins(arr = [3,1,2,4]), 17)
        self.assertEqual(s.sumSubarrayMins(arr = [11,81,94,43,3]), 444)
        


if __name__ == '__main__':
    unittest.main()