from typing import List

class Solution:
    def fib(self, n: int) -> int:
        if n<0:
            return -1
        if n==0 or n==1:
            return n
        dp=[0,1]
        for i in range(2, n+1):
            t=dp[1]
            dp[1]=sum(dp)
            dp[0]=t
        return dp[1]

    def fibRecur(self, n: int) -> int:
        def recur(i, dp1, dp2):
            if i>=n:
                return dp2
            return recur(i+1, dp2, dp1+dp2)

        if n<=1:
            return n
        i,dp1,dp2=2,0,1
        return recur(i, dp1, dp2)



import unittest

class TestSolution(unittest.TestCase):
    def testSubsets(self):
        s = Solution()
        self.assertEqual(s.subsets(nums = [1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        self.assertEqual(s.subsets(nums = [0]), [[],[0]])
        


if __name__ == '__main__':
    unittest.main()