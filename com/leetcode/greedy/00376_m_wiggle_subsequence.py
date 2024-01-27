from typing import List

class Solution:

    # DP use 2 vars to keep track of ascending and descending length
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return 1
        asc,desc=1,1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                asc=desc+1
            elif nums[i]<nums[i-1]:
                desc=asc+1
        return max(asc, desc)


    def wiggleMaxLengthGreedy(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return 1
        if len(nums)==2:
            return 2 if nums[0]!=nums[1] else 1
        asc,r,start=-1,1,0
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            if asc<0:
                asc=1 if nums[i]>nums[i-1] else 0
                r+=1
            elif asc and nums[i]<nums[i-1]:
                asc=0
                r+=1
            elif not asc and nums[i]>nums[i-1]:
                asc=1
                r+=1
        return r




import unittest

class TestSolution(unittest.TestCase):
    def testWiggleMaxLength(self):
        s = Solution()
        self.assertEqual(s.wiggleMaxLength(nums = [1,7,4,9,2,5]), 6)
        self.assertEqual(s.wiggleMaxLength(nums = [1,17,5,10,13,15,10,5,16,8]), 7)
        self.assertEqual(s.wiggleMaxLength(nums = [1,2,3,4,5,6,7,8,9]), 2)
        self.assertEqual(s.wiggleMaxLength(nums = [3,3,3,2,5]), 3)
        


if __name__ == '__main__':
    unittest.main()