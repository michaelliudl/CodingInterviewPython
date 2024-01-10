from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums1 or m<0 or len(nums1)!=m+n:
            return
        i,j,k=m-1,n-1,m+n-1
        while i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i-=1
                k-=1
            elif nums1[i]<nums2[j]:
                nums1[k]=nums2[j]
                j-=1
                k-=1
            else:
                nums1[k]=nums1[i]
                nums1[k-1]=nums2[j]
                i-=1
                j-=1
                k-=2
        while j>=0:
            nums1[j]=nums2[j]
            j-=1
        return

import unittest

class TestSolution(unittest.TestCase):
    def testMerge(self):
        s = Solution()
        nums1 = [1,2,3,0,0,0]
        s.merge(nums1, m = 3, nums2 = [2,5,6], n = 3)
        self.assertEqual(nums1, [1,2,2,3,5,6])

        nums1 = [1]
        s.merge(nums1, m = 1, nums2 = [], n = 0)
        self.assertEqual(nums1, [1])

        nums1 = [0]
        s.merge(nums1, m = 0, nums2 = [1], n = 1)
        self.assertEqual(nums1, [1])


if __name__ == '__main__':
    unittest.main()