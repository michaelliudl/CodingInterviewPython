from typing import List

'''
You are given an integer array ribbons, where ribbons[i] represents the length of the ith ribbon, and an integer k. You may cut any of the ribbons into any number of segments of positive integer lengths, or perform no cuts at all.

For example, if you have a ribbon of length 4, you can:
Keep the ribbon of length 4,
Cut it into one ribbon of length 3 and one ribbon of length 1,
Cut it into two ribbons of length 2,
Cut it into one ribbon of length 2 and two ribbons of length 1, or
Cut it into four ribbons of length 1.
Your goal is to obtain k ribbons of all the same positive integer length. You are allowed to throw away any excess ribbon as a result of cutting.

Return the maximum possible positive integer length that you can obtain k ribbons of, or 0 if you cannot obtain k ribbons of the same length.
'''
class Solution:

    # Binary search between 1 and max value.
    # For each mid, divide each `ribbons` and check if it can give at least `k` segments
    # If yes, decrease `high` otherwise increase `low`
    def maxLength(self, ribbons: List[int], k: int) -> int:

        def canCut(seg):
            count = 0
            for rib in ribbons:
                count += rib // seg
            return count >= k

        if not ribbons:
            return 0
        longest = max(ribbons)
        low, high = 1, longest
        result = 0
        while low <= high:                  # Both inclusive
            mid = low + (high - low) // 2
            if canCut(mid):
                result = max(result, mid)   # Track max viable result on the way
                low = mid + 1
            else:
                high = mid - 1              # Because `high` is included
        return result


import unittest

class TestSolution(unittest.TestCase):
    def testMaxLength(self):
        s = Solution()
        self.assertEqual(s.maxLength(ribbons = [9,7,5], k = 3), 5)
        self.assertEqual(s.maxLength(ribbons = [7,5,9], k = 4), 4)
        self.assertEqual(s.maxLength(ribbons = [5,7,9], k = 22), 0)
        self.assertEqual(s.maxLength(ribbons = [90,7,5], k = 3), 30)


if __name__ == '__main__':
    unittest.main()