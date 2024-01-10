from typing import List

class Solution:
    # O(m+n)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if (not nums1 and not nums2) or (len(nums1)==0 and len(nums2)==0):
            return 0
        if not nums1 or len(nums1) == 0:
            return self.findInSingle(nums2)
        if not nums2 or len(nums2) == 0:
            return self.findInSingle(nums1)
        return self.findInDouble(nums1, nums2)
    
    def findInDouble(self, nums1: List[int], nums2: List[int]) -> float:
        t=len(nums1)+len(nums2)
        odd=t%2==1
        move=int(t/2)
        p,c,i,j=0,0,0,0
        # while i<len(nums1) and j<len(nums2)

        return 0
    
    def findInSingle(self, nums: List[int]) -> float:
        if len(nums)%2==1:
            return nums[int(len(nums)/2)]
        else:
            return (nums[int(len(nums)/2)]+nums[int(len(nums)/2)-1])/2

import unittest

class TestSolution(unittest.TestCase):
    def testFindMedianSortedArrays(self):
        s = Solution()
        self.assertEqual(s.findMedianSortedArrays(nums1 = [1,2,3], nums2 = []), 2.)
        self.assertEqual(s.findMedianSortedArrays(nums1 = [], nums2 = [1,2,3]), 2.)
        self.assertEqual(s.findMedianSortedArrays(nums1 = [1,2,3,4], nums2 = []), 2.5)
        self.assertEqual(s.findMedianSortedArrays(nums1 = [], nums2 = [1,2,3,4]), 2.5)
        self.assertEqual(s.findMedianSortedArrays(nums1 = [1,3], nums2 = [2]), 2.)
        self.assertEqual(s.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]), 2.5)


if __name__ == '__main__':
    unittest.main()