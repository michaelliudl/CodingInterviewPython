from typing import List

class Solution:

    # User map to track count of prefix sum values
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        if not nums:
            return 0
        map = {0:1}
        count = 0
        prefix = 0
        for num in nums:
            prefix += num
            diff = prefix - goal    # Only count when prefix sum is at least goal
            if diff in map:
                count += map[diff]
            map[prefix] = map.get(prefix, 0) + 1
        return count

import unittest

class TestSolution(unittest.TestCase):
    def testNumSubarraysWithSum(self):
        s = Solution()
        self.assertEqual(s.checkSubarraySum(nums = [5,0,0,0], k = 3), True)
        self.assertEqual(s.checkSubarraySum(nums = [0,1,0,3,0,4,0,4,0], k = 5), False)
        self.assertEqual(s.checkSubarraySum(nums = [23,2,4,6,7], k = 6), True)
        self.assertEqual(s.checkSubarraySum(nums = [23,2,6,4,7], k = 6), True)
        self.assertEqual(s.checkSubarraySum(nums = [23,2,6,4,7], k = 13), False)


if __name__ == '__main__':
    unittest.main()