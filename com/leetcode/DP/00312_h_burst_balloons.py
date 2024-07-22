from typing import List
import functools

class Solution:

    # DP Bottom-up, dp[i][j] is max result for subarray between i and j inclusive
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        for d in range(n):
            for i in range(1, n - d + 1):
                j = i + d
                for k in range(i, j + 1):
                    dp[i][j] = max(dp[i][j], dp[i][k - 1] + dp[k + 1][j] + nums[i - 1] * nums[k] * nums[j + 1])
                    
        return dp[1][n]

    # DP Top-down, try to recurse from each index
    def maxCoinsTopDown(self, nums: List[int]) -> int:
        
        @functools.cache
        def dp(start, end):
            if start > end:
                return 0
            return max(dp(start, i - 1) + dp(i + 1, end) + (nums[start - 1] * nums[i] * nums[end + 1]) for i in range(start, end + 1))
        
        n = len(nums)   # Original length
        nums = [1] + nums + [1]     # Add value=1 prefix and suffix
        return dp(1, n)     #  `dp` function returns max result for subarray between 1 and n, inclulsive



import unittest

class TestSolution(unittest.TestCase):
    def testMaxCoins(self):
        s = Solution()
        self.assertEqual(s.maxCoins(nums = [3,1,5,8]), 167)
        self.assertEqual(s.maxCoins(nums = [1,5]), 10)
        


if __name__ == '__main__':
    unittest.main()