from typing import List
import heapq

class Solution:

    # Mono desc stack holding elements and number of subarrays with this element as max and boundary
    def numberOfSubarrays(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 0
        stack = []
        for num in nums:
            while stack and stack[-1][0] < num:     # Pop smaller ones
                stack.pop()
            if stack and stack[-1][0] == num:       # If stack top is same element, increment such subarray count by 1
                stack[-1][1] += 1
            else:
                stack.append([num, 1])              # Each single element is 1 valid subarray
            res += stack[-1][1]
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testNumberOfSubarrays(self):
        s = Solution()
        self.assertEqual(s.numberOfSubarrays(nums = [1,4,3,3,2]), 6)
        self.assertEqual(s.numberOfSubarrays(nums = [3,3,3]), 6)
        self.assertEqual(s.numberOfSubarrays(nums = [1]), 1)


if __name__ == '__main__':
    unittest.main()