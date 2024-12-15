from typing import List

class Solution:

    # Binary search between 1 and the largest value in nums
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        # Return number of operations to make `val` penalty
        def numOps(val):
            ops = 0
            for num in nums:
                ops += ((num - 1) // val)
            return ops

        low, high = 1, max(nums)
        while low < high:
            mid = low + (high - low) // 2
            if numOps(val=mid) <= maxOperations:
                high = mid
            else:
                low = mid + 1
        return low

import unittest

class TestSolution(unittest.TestCase):
    def testSearch(self):
        s = Solution()
        self.assertEqual(s.search([1], 1), 0)
        self.assertEqual(s.search([4,5,6,7,0,1,2], 0), 4)



if __name__ == '__main__':
    unittest.main()