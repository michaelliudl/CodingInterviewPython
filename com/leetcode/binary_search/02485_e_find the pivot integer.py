from typing import List

class Solution:
    def pivotInteger(self, n: int) -> int:
        if n <= 1:
            return n
        total = ((n + 1) * n) // 2
        low, high = 1, n
        while low <= high:
            mid = low + (high - low) // 2
            lowSum = ((mid + 1) * mid) // 2
            highSum = total - lowSum + mid
            if lowSum == highSum:
                return mid
            elif lowSum < highSum:
                low = mid + 1
            else:
                high = mid - 1
        return -1

        

import unittest

class TestSolution(unittest.TestCase):

    def testPivotIndex(self):
        s=Solution()
        self.assertEqual(s.pivotIndex(nums = [1,7,3,6,5,6]), 3)
        self.assertEqual(s.pivotIndex(nums = [2,1,-1]), 0)
        self.assertEqual(s.pivotIndex(nums = [1,2,3]), -1)

if __name__ == '__main__':
    unittest.main()