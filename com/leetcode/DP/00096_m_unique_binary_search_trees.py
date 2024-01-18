from typing import List

class Solution:

    # dp[i] # of BSTs with i nodes
    # dp[i] += dp[j-1] * dp[i-j], j in [1, i]
    def numTrees(self, n: int) -> int:
        if n<=0: return n
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            for j in range(1,i+1):
                dp[i]+=dp[j-1]*dp[i-j]
        return dp[n]


import unittest

class TestSolution(unittest.TestCase):
    def testNumTrees(self):
        s = Solution()
        self.assertEqual(s.numTrees(3), 5)
        self.assertEqual(s.numTrees(4), 14)
        self.assertEqual(s.numTrees(5), 42)
        self.assertEqual(s.numTrees(10), 16796)
        


if __name__ == '__main__':
    unittest.main()