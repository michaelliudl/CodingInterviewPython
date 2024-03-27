from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        if not nums:
            return False
        rotated = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if rotated:
                    return False
                rotated = True
            if rotated and nums[i] > nums[0]:
                return False
        return True

        

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def testSortedSquares(self):
        self.assertEqual(self.s.sortedSquares([-4,-1,0,3,10]), [0,1,9,16,100])
        self.assertEqual(self.s.sortedSquares([-7,-3,2,3,11]), [4,9,9,49,121])

if __name__ == '__main__':
    unittest.main()