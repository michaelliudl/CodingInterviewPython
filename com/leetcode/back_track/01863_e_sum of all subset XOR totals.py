from typing import List

class Solution:

    # Backtrack each index and calculate result by including or not including each element
    def subsetXORSum(self, nums: List[int]) -> int:

        def backtrack(index, result):
            if index == len(nums):
                return result
            return backtrack(index + 1, result) + backtrack(index + 1, result ^ nums[index])
        
        return backtrack(index=0, result=0)

import unittest

class TestSolution(unittest.TestCase):
    def testCountArrangement(self):
        s = Solution()
        self.assertEqual(s.countArrangement(n = 2), 2)
        self.assertEqual(s.countArrangement(n = 1), 1)
        


if __name__ == '__main__':
    unittest.main()