from typing import List

class Solution:

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums or k<=0: return False
        n,d=len(nums),{}
        for i in range(n):
            if nums[i] in d:
                d[nums[i]].append(i)
            else:
                d[nums[i]]=[i]
        for _,v in d.items():
            if len(v)>1:
                for i in range(len(v)-1):
                    if v[i+1]-v[i]<=k:
                        return True
        return False
        

        

import unittest

class TestSolution(unittest.TestCase):

    def testPivotIndex(self):
        s=Solution()
        self.assertEqual(s.pivotIndex(nums = [1,7,3,6,5,6]), 3)
        self.assertEqual(s.pivotIndex(nums = [2,1,-1]), 0)
        self.assertEqual(s.pivotIndex(nums = [1,2,3]), -1)

if __name__ == '__main__':
    unittest.main()