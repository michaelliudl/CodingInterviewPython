from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        if not nums or k <= 0:
            return 0
        maxNum = max(nums)
        result = 0
        count = 0
        left = 0
        for num in nums:
            count += 1 if num == maxNum else 0
            # Keep window to include (k - 1) max element
            while count == k:
                if nums[left] == maxNum:
                    count -= 1
                left += 1
            # When left > 0, it's number of subarrays that satisfy the requirement
            result += left
        return result

import unittest

class TestSolution(unittest.TestCase):
    def testCountCompleteSubarrays(self):
        s = Solution()
        self.assertEqual(s.countCompleteSubarrays(nums = [5,5,5,5]), 10)
        self.assertEqual(s.countCompleteSubarrays(nums = [1,3,1,2,2]), 4)


if __name__ == '__main__':
    unittest.main()