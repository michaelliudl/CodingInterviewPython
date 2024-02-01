from typing import List

class Solution:

    # Sort then check diff for every 3
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        if not nums or k<=0 or len(nums)<3 or len(nums)%3!=0: return []
        nums.sort()
        n,r=len(nums),[]
        for i in range(2,n,3):
            if nums[i]-nums[i-2]>k:
                return []
            r.append([nums[i-2],nums[i-1],nums[i]])
        return r

import unittest

class TestSolution(unittest.TestCase):
    def testDivideArray(self):
        s = Solution()
        self.assertEqual(s.divideArray(nums = [1,3,4,8,7,9,3,5,1], k = 2), [[1,1,3],[3,4,5],[7,8,9]])
        self.assertEqual(s.divideArray(nums = [1,3,3,2,7,3], k = 3), [])
        


if __name__ == '__main__':
    unittest.main()