from typing import List

class Solution:

    # For each inside element, greedily count elements smaller/larger before it and larger/smaller after it
    # Add to final result (smaller before) * (larger after) and (larger before) * (smaller after)
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        for i in range(1, len(rating) - 1):
            smallerBefore = largerBefore = 0
            for j in range(i):
                smallerBefore += 1 if rating[j] < rating[i] else 0
                largerBefore += 1 if rating[j] > rating[i] else 0
            smallerAfter = largerAfter = 0
            for j in range(i + 1, len(rating)):
                smallerAfter += 1 if rating[j] < rating[i] else 0
                largerAfter += 1 if rating[j] > rating[i] else 0
            res += ((smallerBefore * largerAfter) + (largerBefore * smallerAfter))
        return res


import unittest

class TestSolution(unittest.TestCase):
    def testMinOperations(self):
        s = Solution()
        self.assertEqual(s.minOperations(k = 11), 5)
        self.assertEqual(s.minOperations(k = 1), 0)


if __name__ == '__main__':
    unittest.main()