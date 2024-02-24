from typing import List

class Solution:

    def missingNumber(self, nums: List[int]) -> int:
        if not nums: return -1
        n,s = len(nums),sum(nums)
        return (n*(n+1))//2 - s

        

import unittest

class TestSolution(unittest.TestCase):

    def testPivotIndex(self):
        s=Solution()
        self.assertEqual(s.pivotIndex(nums = [1,7,3,6,5,6]), 3)
        self.assertEqual(s.pivotIndex(nums = [2,1,-1]), 0)
        self.assertEqual(s.pivotIndex(nums = [1,2,3]), -1)

if __name__ == '__main__':
    unittest.main()