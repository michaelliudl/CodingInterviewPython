from typing import List

class Solution:

    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res = 0
        prev = values[0]
        for i in range(1, len(values)):
            res = max(res, values[i] + prev - i)
            prev = max(prev, values[i] + i)
        return res


import unittest

class TestSolution(unittest.TestCase):
    def testCanJump(self):
        s = Solution()
        self.assertEqual(s.canJump(nums = [2,3,1,1,4]), True)
        self.assertEqual(s.canJump(nums = [3,2,1,0,4]), False)
        


if __name__ == '__main__':
    unittest.main()