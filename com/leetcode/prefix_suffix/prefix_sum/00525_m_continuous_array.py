from typing import List

class Solution:

    # Use prefix sum to track number of '0's and '1's
    # Use hash table to track diffs, only add diff to hash table if not exists
    # Max length possible when prefix value exists in hash table
    def findMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxLen = prefix = 0
        map = {0: -1}
        for i, num in enumerate(nums):
            if num == 1:
                prefix += 1
            else:
                prefix -= 1
            if prefix in map:
                maxLen = max(maxLen, (i - map[prefix]))
            else:
                map[prefix] = i
        return maxLen


import unittest

class TestSolution(unittest.TestCase):
    def testCheckSubarraySum(self):
        s = Solution()
        self.assertEqual(s.checkSubarraySum(nums = [5,0,0,0], k = 3), True)
        self.assertEqual(s.checkSubarraySum(nums = [0,1,0,3,0,4,0,4,0], k = 5), False)
        self.assertEqual(s.checkSubarraySum(nums = [23,2,4,6,7], k = 6), True)
        self.assertEqual(s.checkSubarraySum(nums = [23,2,6,4,7], k = 6), True)
        self.assertEqual(s.checkSubarraySum(nums = [23,2,6,4,7], k = 13), False)


if __name__ == '__main__':
    unittest.main()