from typing import List

class Solution:

    # Sort then Binary search within [0, max(nums)]
    # For each middle value, use sliding window to find number of pairs with diff <= middle value
    def smallestDistancePair(self, nums: List[int], k: int) -> int:

        def countPairs(diff):
            res = left = 0
            for i in range(len(nums)):
                while nums[left] + diff < nums[i]:
                    left += 1
                res += (i - left)
            return res

        nums.sort()
        low, high = 0, (nums[-1] - nums[0])     # Upper bound is (max - min)
        while low < high:
            mid = low + (high - low) // 2
            res = countPairs(mid)
            if res >= k:    # If more pairs than `k`, `mid` could be the result
                high = mid
            else:
                low = mid + 1
        return low

import unittest

class TestSolution(unittest.TestCase):
    def testSmallestDistancePair(self):
        s = Solution()
        self.assertEqual(s.smallestDistancePair(nums = [1,3,1], k = 1), 0)
        self.assertEqual(s.smallestDistancePair(nums = [1,1,1], k = 2), 0)
        self.assertEqual(s.smallestDistancePair(nums = [1,6,1], k = 3), 5)


if __name__ == '__main__':
    unittest.main()