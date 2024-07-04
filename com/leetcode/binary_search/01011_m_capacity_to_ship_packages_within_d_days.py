from typing import List

class Solution:

    # Similar to 410. Binary search within [max(weights), sum(weights)] for capacity limit
    # Then greedily verify if can be split into `days` or fewer subarrays whose sum are all less than or equal to limit
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canSplit(limit):
            curSum,subCount = 0,1
            for weight in weights:
                curSum += weight
                if curSum > limit:
                    subCount += 1
                    curSum = weight
            return subCount <= days

        if not weights: return 0
        low,high = max(weights),sum(weights)
        ans = high
        while low < high:
            mid = low + (high-low)//2
            if canSplit(mid):
                ans = min(ans, mid)
                high = mid
            else:
                low = mid + 1
        return ans


import unittest

class TestSolution(unittest.TestCase):
    def testShipWithinDays(self):
        s = Solution()
        self.assertEqual(s.shipWithinDays(weights = [1,2,3,4,5,6,7,8,9,10], days = 5), 15)
        self.assertEqual(s.shipWithinDays(weights = [3,2,2,4,1,4], days = 3), 6)
        self.assertEqual(s.shipWithinDays(weights = [1,2,3,1,1], days = 4), 3)


if __name__ == '__main__':
    unittest.main()