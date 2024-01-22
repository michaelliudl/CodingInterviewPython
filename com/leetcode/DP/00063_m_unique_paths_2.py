from typing import List

class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        dp=[[0]*n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0]==1:
                break
            dp[i][0]=1
        for j in range(n):
            if obstacleGrid[0][j]==1:
                break
            dp[0][j]=1
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]!=1:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
    
    def uniquePathsWithObstaclesOneDArray(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        dp=[1]*n
        for j in range(n):
            if obstacleGrid[0][j]==1 or (j>0 and dp[j-1]==0):
                dp[j]=0
        for i in range(1,m):
            for j in range(n):
                if obstacleGrid[i][j]==1:
                    dp[j]=0
                elif j>0:
                    dp[j]+=dp[j-1]
        return dp[n-1]



import unittest

class TestSolution(unittest.TestCase):
    def testSubsets(self):
        s = Solution()
        self.assertEqual(s.subsets(nums = [1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        self.assertEqual(s.subsets(nums = [0]), [[],[0]])
        


if __name__ == '__main__':
    unittest.main()