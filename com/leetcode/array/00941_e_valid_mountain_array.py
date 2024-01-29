from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if not arr or len(arr)<3: return False
        maxIndex=0
        for i in range(1,len(arr)):
            if arr[i]>arr[maxIndex]:
                maxIndex=i
        if maxIndex==0 or maxIndex==len(arr)-1:
            return False
        for i in range(len(arr)):
            if i<maxIndex and arr[i]>=arr[i+1]:
                return False
            if i>=maxIndex and i<len(arr)-1 and arr[i]<=arr[i+1]:
                return False
        return True

        

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def testSortedSquares(self):
        self.assertEqual(self.s.sortedSquares([-4,-1,0,3,10]), [0,1,9,16,100])
        self.assertEqual(self.s.sortedSquares([-7,-3,2,3,11]), [4,9,9,49,121])

if __name__ == '__main__':
    unittest.main()