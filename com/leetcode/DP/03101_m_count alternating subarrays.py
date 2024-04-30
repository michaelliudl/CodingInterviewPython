from typing import List

class Solution:

    # Simplified to 1D DP array
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                dp[i] += dp[i - 1]
        return sum(dp)

    # dp is 2 rows n columns array
    # dp[0][i] is count of alternating subarrays ending at index `i` when nums[i] == 0
    # dp[1][i] is count of alternating subarrays ending at index `i` when nums[i] == 1
    # Loop nums array backwards
    def countAlternatingSubarrays2D(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [[0] * n, [0] * n]
        if nums[n - 1] == 1:
            dp[1][n - 1] = 1
        else:
            dp[0][n - 1] = 1
        for i in range(n - 2, -1, -1):
            if nums[i] == 0:
                dp[0][i] = dp[1][i + 1] + 1
            else:
                dp[1][i] = dp[0][i + 1] + 1
        result = 0
        for i in range(n):
            result += max(dp[0][i], dp[1][i])
        return result


import unittest

class TestSolution(unittest.TestCase):
    def testLargestDivisibleSubset(self):
        s = Solution()
        self.assertEqual(s.largestDivisibleSubset(nums = [1,2,3]), [2,1])
        self.assertEqual(s.largestDivisibleSubset(nums = [1,2,4,8]), [8,4,2,1])
        


if __name__ == '__main__':
    unittest.main()