from typing import List

class Solution:

    # Sort, for each element, keep min possible value for next in unique array
    # If num < next min possible value, need to increment it per diff
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        minPossible = 0
        res = 0
        for num in nums:
            res += max(minPossible - num, 0)
            minPossible = max(minPossible, num) + 1
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testBagOfTokensScore(self):
        s = Solution()
        self.assertEqual(s.bagOfTokensScore(tokens = [33,4,28,24,96], power = 35), 3)
        self.assertEqual(s.bagOfTokensScore(tokens = [100], power = 50), 0)
        self.assertEqual(s.bagOfTokensScore(tokens = [200,100], power = 150), 1)
        self.assertEqual(s.bagOfTokensScore(tokens = [100,200,300,400], power = 200), 2)


if __name__ == '__main__':
    unittest.main()