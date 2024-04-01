from typing import List

class Solution:

    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        if not nums:
            return 0
        result = 0
        left = 0
        minIndex = maxIndex = -1
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                minIndex = maxIndex = -1
                left = i + 1
            if num == minK:
                minIndex = i
            if num == maxK:
                maxIndex = i
            result += max(0, min(minIndex, maxIndex) - left + 1)
        return result


import unittest

class TestSolution(unittest.TestCase):
    def testCountSubarrays(self):
        s = Solution()
        self.assertEqual(s.countSubarrays(nums = [1,3,5,2,7,5], minK = 1, maxK = 5), 2)
        self.assertEqual(s.countSubarrays(nums = [1,1,1,1], minK = 1, maxK = 1), 10)


if __name__ == '__main__':
    unittest.main()