from typing import List
import heapq,math

class Solution:

    # Complete Backpack of n and items are perfect squares up to sqrt(n)

    # dp[j] is min number of perfects that sum up to n
    # dp[j] = min(dp[j], dp[j-square(i)] + 1)
    def numSquares(self, n: int) -> int:
        if n<=0:
            return 0
        sq=int(math.sqrt(n))+1
        dp=[float('inf')]*(n+1)
        dp[0]=0
        for i in range(1,sq+1):
            for j in range(i*i,n+1):
                dp[j]=min(dp[j], dp[j - i*i] + 1)
        return dp[n]


import unittest

class TestSolution(unittest.TestCase):
    def testNumSquares(self):
        s = Solution()
        self.assertEqual(s.numSquares(n=12), 3)
        self.assertEqual(s.numSquares(n=13), 2)



if __name__ == '__main__':
    unittest.main()