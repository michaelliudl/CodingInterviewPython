from typing import List

class Solution:

    # dp[i]     is max size of subset that ends at i and meet requirement
    # prev[i]   is previous index of the element in the largest subset
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums: return []
        nums.sort()     # Need to sort first
        n = len(nums)
        dp, prev = [0] * n, [-1] * n
        maxLen, maxIndex = 0, 0
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
                        if dp[i] > maxLen:
                            maxLen = dp[i]
                            maxIndex = i
        ans = []
        while maxIndex > -1:
            ans.append(nums[maxIndex])
            maxIndex = prev[maxIndex]
        return ans


import unittest

class TestSolution(unittest.TestCase):
    def testLargestDivisibleSubset(self):
        s = Solution()
        self.assertEqual(s.largestDivisibleSubset(nums = [1,2,3]), [2,1])
        self.assertEqual(s.largestDivisibleSubset(nums = [1,2,4,8]), [8,4,2,1])
        


if __name__ == '__main__':
    unittest.main()