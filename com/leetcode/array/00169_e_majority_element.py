from typing import List

class Solution:

    # Hash O(n) space
    # 
    # Moore's Voting Algorithm O(1) space
    def majorityElement(self, nums: List[int]) -> int:
        if not nums: return 0
        candidate,count=None,0
        for num in nums:
            if count==0:
                candidate=num
            if num==candidate:
                count+=1
            else:
                count-=1
        return candidate

        

import unittest

class TestSolution(unittest.TestCase):

    def testPivotIndex(self):
        s=Solution()
        self.assertEqual(s.pivotIndex(nums = [1,7,3,6,5,6]), 3)
        self.assertEqual(s.pivotIndex(nums = [2,1,-1]), 0)
        self.assertEqual(s.pivotIndex(nums = [1,2,3]), -1)

if __name__ == '__main__':
    unittest.main()