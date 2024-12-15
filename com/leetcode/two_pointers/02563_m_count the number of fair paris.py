from typing import List

class Solution:
    
    # Sort then use two pointers to find count of pairs of both lower/upper limits
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:

        def count(bound):
            count = 0
            low = 0
            high = len(nums) - 1
            while low < high:
                while low < high and (nums[low] + nums[high]) > bound:
                    high -= 1
                count += (high - low)
                low += 1
            return count

        nums.sort()
        return count(upper) - count(lower - 1)


import unittest

class TestSolution(unittest.TestCase):
    def testMaxArea(self):
        s = Solution()
        self.assertEqual(s.maxArea(height = [1,8,6,2,5,4,8,3,7]), 49)
        self.assertEqual(s.maxArea(height = [1,1]), 1)


if __name__ == '__main__':
    unittest.main()