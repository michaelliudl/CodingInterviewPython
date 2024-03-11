from typing import List,Deque

class Solution:

    # Create new DP array for each move and update from previous move's DP array
    # Add dp[i][j] to result if next move of i,j is out
    # nextDP[x][y] += dp[x][y]    Update with count with number of paths from previous move's DP array
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        def out(row,col):
            return row<0 or col<0 or row>=m or col>=n

        if m<=0 or n<=0 or maxMove<=0 or startRow<0 or startColumn<0 or startRow>=m or startColumn>=n:
            return 0
        
        MOD=10**9+7
        dirs=[(-1,0),(1,0),(0,-1),(0,1)]
        dp=[[0]*n for _ in range(m)]
        dp[startRow][startColumn]=1
        r=0

        for move in range(maxMove):
            newDP=[[0]*n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if dp[i][j]>0:
                        for a,b in dirs:
                            x,y=i+a,j+b
                            if out(x,y):
                                r+=dp[i][j]
                                r%=MOD
                            else:
                                newDP[x][y]+=dp[i][j]
                                newDP[x][y]%=MOD
            dp=newDP
        return r

    
    # Time out
    def findPathsBrute(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        dirs=[(-1,0),(1,0),(0,-1),(0,1)]

        def out(row,col):
            return row<0 or col<0 or row>=m or col>=n

        def recur(row,col,rem):
            nonlocal r
            if out(row,col) and rem>=0:
                r+=1
                return
            if rem==0:
                return
            for a,b in dirs:
                recur(row+a,col+b,rem-1)

        if m<=0 or n<=0 or maxMove<=0 or startRow<0 or startColumn<0 or startRow>=m or startColumn>=n:
            return 0
        r=0
        recur(startRow,startColumn,rem=maxMove)
        return r

        

import unittest

class TestSolution(unittest.TestCase):
    def testFindPaths(self):
        s = Solution()
        self.assertEqual(s.findPaths(m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0), 6)
        self.assertEqual(s.findPaths(m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1), 12)
        


if __name__ == '__main__':
    unittest.main()