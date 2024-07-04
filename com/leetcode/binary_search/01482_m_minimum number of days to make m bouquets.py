from typing import List

class Solution:

    # Similar to 410 and 1011
    # Binary search between min/max value of given array, until converge on min value that satisfies the condition
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        # Return number of bouquets can be made after `cur` days
        def make(cur):
            count = 0
            needed = k
            for day in bloomDay:
                if day > cur:
                    needed = k      # Reset after condition not met
                else:
                    needed -= 1     # Greedily take first values meeting condition
                    if needed == 0:
                        count += 1
                        needed = k
            return count

        n = len(bloomDay)
        if n < m * k:
            return -1
        low, high = min(bloomDay), max(bloomDay)
        while low < high:
            mid = low + (high - low) // 2
            if make(mid) >= m:
                high = mid
            else:
                low = mid + 1
        return low


import unittest

class TestSolution(unittest.TestCase):
    def testMinDays(self):
        s = Solution()
        self.assertEqual(s.minDays(bloomDay = [1,10,3,10,2], m = 3, k = 1), 3)
        self.assertEqual(s.minDays(bloomDay = [1,10,3,10,2], m = 3, k = 2), -1)
        self.assertEqual(s.minDays(bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3), 12)


if __name__ == '__main__':
    unittest.main()