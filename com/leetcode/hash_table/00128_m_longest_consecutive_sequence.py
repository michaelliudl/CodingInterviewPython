from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        candidates=set(nums)
        ans = 0
        for num in nums:
            if num-1 in candidates:     # Find starting number of potential consecutives
                continue
            curLen = 0
            while num in candidates:
                num += 1
                curLen += 1
            ans = max(ans, curLen)
        return ans

import unittest

class TestSolution(unittest.TestCase):
    def testTwoSum(self):
        s = Solution()
        self.assertEqual(s.twoSum([2,7,11,15],9), [0,1])
        self.assertEqual(s.twoSum([3,2,4],6), [1,2])
        self.assertEqual(s.twoSum([3,3],6), [0,1])


if __name__ == '__main__':
    unittest.main()