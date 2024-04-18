from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if not nums: return 0
        ans,slow,toDelete=0,0,0
        for i in range(len(nums)):
            if nums[i] == 0:
                toDelete += 1
            while toDelete > 1:
                if nums[slow] == 0:
                    toDelete -= 1
                slow += 1
            ans = max(ans, (i-slow))
        return ans



import unittest

class TestSolution(unittest.TestCase):
    def testLongestSubarray(self):
        s = Solution()
        self.assertEqual(s.longestSubarray(nums = [0,1,1,1,0,1,1,0,1]), 5)
        self.assertEqual(s.longestSubarray(nums = [1,1,0,1]), 3)
        self.assertEqual(s.longestSubarray(nums = [1,1,1]), 2)


if __name__ == '__main__':
    unittest.main()