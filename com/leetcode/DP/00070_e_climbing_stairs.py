from typing import List

class Solution:
    # dp[n]=dp[n-1]+dp[n-2]
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        dp=[1,2]
        for i in range(3,n+1):
            t=dp[1]
            dp[1]=dp[0]+dp[1]
            dp[0]=t
        return dp[1]


import unittest

class TestSolution(unittest.TestCase):
    def testSubsets(self):
        s = Solution()
        self.assertEqual(s.subsets(nums = [1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        self.assertEqual(s.subsets(nums = [0]), [[],[0]])
        


if __name__ == '__main__':
    unittest.main()