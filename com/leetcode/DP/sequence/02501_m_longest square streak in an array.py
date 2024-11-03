from typing import List

class Solution:

    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort(reverse=True)     # Sort reversed to accumulate streak count at square root value
        maxVal = nums[0]
        dp = [0] * (maxVal + 1)     # dp[i] := longest square streak starts with value i
        for num in nums:
            dp[num] = 1
            square = num * num
            if square <= maxVal:
                dp[num] += dp[square]
        res = max(dp)
        return res if res >= 2 else -1



import unittest

class TestSolution(unittest.TestCase):
    def testLongestSquareStreak(self):
        s = Solution()
        self.assertEqual(s.longestSquareStreak(nums = [4,3,6,16,8,2]), 3)
        self.assertEqual(s.longestSquareStreak(nums = [2,3,5,6,7]), -1)
        


if __name__ == '__main__':
    unittest.main()