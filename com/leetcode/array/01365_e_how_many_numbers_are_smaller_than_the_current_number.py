from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        if not nums: return []
        numsSort=nums[:]
        numsSort.sort()
        d={}
        for i in range(len(numsSort)):
            if not numsSort[i] in d:
                d[numsSort[i]]=i
        r=[0]*len(nums)
        for i in range(len(nums)):
            r[i]=d[nums[i]]
        return r
        

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def testSortedSquares(self):
        self.assertEqual(self.s.sortedSquares([-4,-1,0,3,10]), [0,1,9,16,100])
        self.assertEqual(self.s.sortedSquares([-7,-3,2,3,11]), [4,9,9,49,121])

if __name__ == '__main__':
    unittest.main()