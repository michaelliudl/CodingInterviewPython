from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        if not nums or len(nums)<2:
            return nums
        d={}
        dup=0
        for v in nums:
            if v in d:
                dup=v
                break
            else:
                d[v]=1
        diff=sum(nums)-sum([i for i in range(1,len(nums)+1)])
        return [dup, dup-diff]

import unittest

class TestSolution(unittest.TestCase):
    def testFindErrorNums(self):
        s = Solution()
        self.assertEqual(s.findErrorNums(nums = [1,2,2,4]), [2,3])
        self.assertEqual(s.findErrorNums(nums = [1,1]), [1,2])
        self.assertEqual(s.findErrorNums(nums = [2,2]), [2,1])
        


if __name__ == '__main__':
    unittest.main()