from typing import List

class Solution:

    def candy(self, ratings: List[int]) -> int:
        if not ratings: return 0
        if len(ratings)==1: return 1
        n=len(ratings)
        canLeft,canRight=[1]*n,[1]*n
        # Left to right
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                canLeft[i]=canLeft[i-1]+1
            else:
                canLeft[i]=1
        # Right to left
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                canRight[i]=canRight[i+1]+1
            else:
                canRight[i]=1
        for i in range(n):
            canLeft[i]=max(canLeft[i], canRight[i])
        return sum(canLeft)


import unittest

class TestSolution(unittest.TestCase):
    def testCandy(self):
        s = Solution()
        self.assertEqual(s.candy(ratings = [1,0,2]), 5)
        self.assertEqual(s.candy(ratings = [1,2,2]), 4)
        self.assertEqual(s.candy(ratings = [1,2,87,87,87,2,1]), 13)
        


if __name__ == '__main__':
    unittest.main()