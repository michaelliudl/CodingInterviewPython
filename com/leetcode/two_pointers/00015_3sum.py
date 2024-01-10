from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums)<3:
            return None
        nums.sort()
        s=set()
        ln=len(nums)
        for i in range(ln-2):
            j,k=i+1,ln-1
            while j<k:
                sum=nums[i]+nums[j]+nums[k]
                if sum==0:
                    s.add(tuple([nums[i],nums[j],nums[k]]))
                    j+=1
                elif sum<0:
                    j+=1
                else:
                    k-=1
        return [list(e) for e in s]

import unittest

class TestSolution(unittest.TestCase):
    def testThreeSum(self):
        s = Solution()
        self.assertEqual(s.threeSum([-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]])
        self.assertEqual(s.threeSum([0,1,1]), [])
        self.assertEqual(s.threeSum([0,0,0]), [[0,0,0]])


if __name__ == '__main__':
    unittest.main()