from typing import List

class Solution:

    # Brute force loop and backtrack recursion

    # Each string in array is one item. Its weight is two dimensional with # of 0s and # of 1s. It's value is 1 which is to add to the # of subsets.
    # dp[i][j] is max # of subsets with at most i 0s and j 1s.
    # dp[i][j] = max(dp[i][j], dp[i-(# of 0s in string k)][i-(# of 1s in string k)] + 1)    Decide to put string k into backpack or not
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        if not strs or m<=0 or n<=0:
            return 0
        dp=[[0]*(n+1) for _ in range(m+1)]    # Backpack size initialized with constraint
        for s in strs:
            numZeros=sum([1 for c in s if c=='0'])
            numOnes=len(s)-numZeros
            for i in range(m, numZeros-1, -1):
                for j in range(n, numOnes-1, -1):
                    dp[i][j]=max(dp[i][j], dp[i-numZeros][j-numOnes] + 1)
        return dp[m][n]

        

import unittest

class TestSolution(unittest.TestCase):
    def testFindMaxForm(self):
        s = Solution()
        self.assertEqual(s.findMaxForm(strs = ["10","0001","111001","1","0"], m = 5, n = 3), 4)
        self.assertEqual(s.findMaxForm(strs = ["10","0","1"], m = 1, n = 1), 2)


if __name__ == '__main__':
    unittest.main()