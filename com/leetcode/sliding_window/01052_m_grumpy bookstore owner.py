from typing import List

class Solution:

    # Fixed size sliding window to find maximum flipped value sum in the window
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        total = sum(customers[i] for i in range(n) if grumpy[i] == 0)   # No need to flip
        maxFlipped = curFlipped = 0
        for i in range(n):
            if grumpy[i] == 1:      # Add a new flipped value to window sum
                curFlipped += customers[i]
            if i >= minutes and grumpy[i - minutes] == 1:   # Remove out of window flipped value
                curFlipped -= customers[i - minutes]
            maxFlipped = max(maxFlipped, curFlipped)
        res = total + maxFlipped
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testSubarraysWithKDistinct(self):
        s = Solution()
        self.assertEqual(s.subarraysWithKDistinct(nums = [1,2,1,2,3], k = 2), 7)
        self.assertEqual(s.subarraysWithKDistinct(nums = [1,2,1,3,4], k = 3), 3)


if __name__ == '__main__':
    unittest.main()