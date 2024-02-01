from typing import List

class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums: return nums
        n=len(nums)
        fw,bw=[1]*n,[1]*n
        for i in range(1,n):
            fw[i]=nums[i-1]*fw[i-1]
        for i in range(n-2,-1,-1):
            bw[i]=nums[i+1]*bw[i+1]
        for i in range(n):
            fw[i]*=bw[i]
        return fw
        

        

import unittest

class TestSolution(unittest.TestCase):

    def testInsert(self):
        s=Solution()
        self.assertEqual(s.insert(intervals = [], newInterval = [5,7]), [[5,7]])
        self.assertEqual(s.insert(intervals = [[1,3],[6,9]], newInterval = [2,5]), [[1,5],[6,9]])
        self.assertEqual(s.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]), [[1,2],[3,10],[12,16]])

if __name__ == '__main__':
    unittest.main()