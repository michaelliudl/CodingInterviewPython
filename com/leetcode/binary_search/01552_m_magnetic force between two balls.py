from typing import List

class Solution:

    # Sort then binary search
    # Lower bound = 1 (min distance), upper bound = (max value - min value)
    def maxDistance(self, position: List[int], m: int) -> int:

        def numberInRangeWithDiff(diff):
            num = 1
            prev = position[0]
            for i in range(1, len(position)):
                if position[i] - prev >= diff:
                    num += 1
                    prev = position[i]
            return num 

        position.sort()
        low, high = 1, (position[-1] - position[0])
        while low < high:
            mid = high - (high - low) // 2          # Converge on max of diff
            if numberInRangeWithDiff(mid) < m:      # With current diff `mid`, how many can fit in range
                high = mid - 1
            else:
                low = mid
        return low

import unittest

class TestSolution(unittest.TestCase):
    def testMaxDistance(self):
        s = Solution()
        self.assertEqual(s.maxDistance(position = [1,2,3,4,7], m = 3), 3)
        self.assertEqual(s.maxDistance(position = [5,4,3,2,1,1000000000], m = 2), 999999999)


if __name__ == '__main__':
    unittest.main()