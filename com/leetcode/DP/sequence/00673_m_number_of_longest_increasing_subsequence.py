from typing import List

class Solution:

    # Need 2 states
    # dp[i]     Length of LIS at i
    # count[i]  Number of LIS at i
    #
    # Loop before i as j and only need nums[i]>nums[j]
    # 
    # dp[i] = max(dp[i], dp[j]+1) when nums[i]>nums[j] (0 <= j < i)     Compare dp[i] and dp[j]+1
    # count[i] = count[j] when dp[j]+1 > dp[i]                          Found a longer LIS, update count to it's count
    # count[i] += count[j] when dp[j]+1 == dp[j]                        Same length LIS, accumulate total count
    #
    # Sum all counts i where i matches max length in dp[i]
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        n=len(nums)
        dp,count=[1]*n,[1]*n
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j]:
                    if dp[j]+1 > dp[i]:
                        count[i]=count[j]
                    elif dp[j]+1 == dp[i]:
                        count[i] += count[j]
                    dp[i]=max(dp[i], dp[j]+1)
        maxLIS=max(dp)
        r=0
        for i in range(n):
            if dp[i] == maxLIS:
                r += count[i]
        return r

import unittest

class TestSolution(unittest.TestCase):
    def testFindNumberOfLIS(self):
        s = Solution()
        self.assertEqual(s.findNumberOfLIS(nums = [1,3,5,4,7]), 2)
        self.assertEqual(s.findNumberOfLIS(nums = [2,2,2,2,2]), 5)
        


if __name__ == '__main__':
    unittest.main()