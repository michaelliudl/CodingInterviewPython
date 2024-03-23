from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower, upper]]
        result = []
        start = lower
        for num in nums:
            if num > start:
                result.append([start, num - 1])
            start = num + 1
        if nums[-1] < upper:
            result.append([nums[-1] + 1, upper])
        return result
    
import unittest

class TestSolution(unittest.TestCase):
    def testFindMissingRanges(self):
        s = Solution()
        self.assertEqual(s.findMissingRanges(nums = [0,1,3,50,75], lower = 0, upper = 99), [[2,2],[4,49],[51,74],[76,99]])
        self.assertEqual(s.findMissingRanges(nums = [-1], lower = -1, upper = -1), [])


if __name__ == '__main__':
    unittest.main()
