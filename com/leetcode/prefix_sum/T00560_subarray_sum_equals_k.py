from typing import List

class Solution:

    # Prefix sum and use hash table to cache diff
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums: return 0
        ans, left, curSum = 0, 0, 0
        for i in range(len(nums)):
            curSum += nums[i]
            if curSum == k:
                ans += 1
            
        return ans


import unittest

class TestSolution(unittest.TestCase):
    def testSimplifyPath(self):
        s = Solution()
        self.assertEqual(s.simplifyPath("/home/"), "/home")
        self.assertEqual(s.simplifyPath("/../"), "/")
        self.assertEqual(s.simplifyPath("/home//foo/"), "/home/foo")



if __name__ == '__main__':
    unittest.main()