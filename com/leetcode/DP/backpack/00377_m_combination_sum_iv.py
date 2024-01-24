from typing import List

class Solution:

    # Order of numbers matters in combination, so it's actually permutation

    # dp[i] is number of permutations of elements that sum to i
    # dp[i] += dp[i - nums(j)]
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums or target<0:
            return 0
        dp=[0]*(target+1)
        dp[0]=1
        for i in range(target+1):           # Loop backpack first for permutation of elements
            for j in range(len(nums)):      # Both loop forwards
                if i-nums[j]>=0:
                    dp[i]+=dp[i-nums[j]]
        return dp[target]
        

import unittest

class TestSolution(unittest.TestCase):
    def testCombinationSum4(self):
        s = Solution()
        self.assertEqual(s.combinationSum4(nums = [1,2,3], target = 4), 7)
        self.assertEqual(s.combinationSum4(nums = [9], target = 3), 0)


if __name__ == '__main__':
    unittest.main()