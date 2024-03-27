from typing import List
import math
class Solution:

    # (long(m+n))   Use quick select
    def findMedianSortedArraysQuickSelect(self, nums1: List[int], nums2: List[int]) -> float:

        def findKthInTwoSortedArray(nums1, start1, nums2, start2, k):
            remaining1 = len(nums1) - start1
            remaining2 = len(nums2) - start2
            if remaining1 > remaining2:
                return findKthInTwoSortedArray(nums2, start2, nums1, start1, k)
            if remaining1 == 0:
                return nums2[start2 + k - 1]
            if k == 1:
                return min(nums1[start1], nums2[start2])
            # Divide k into 2 parts
            half = k // 2
            lenHalfKth1 = half if remaining1 > half else remaining1
            lenHalfKth2 = k - lenHalfKth1
            halfKth1 = nums1[start1 + lenHalfKth1 - 1]
            halfKth2 = nums2[start2 + lenHalfKth2 - 1]
            if halfKth1 < halfKth2:
                return findKthInTwoSortedArray(nums1, start1 + lenHalfKth1, nums2, start2, k - lenHalfKth1)
            elif halfKth1 > halfKth2:
                return findKthInTwoSortedArray(nums1, start1, nums2, start2 + lenHalfKth2, k - lenHalfKth2)
            else:
                return halfKth1

        # Edge cases
        if (not nums1 and not nums2) or (len(nums1)==0 and len(nums2)==0):
            return 0
        if not nums1 or len(nums1) == 0:
            return self.findInSingle(nums2)
        if not nums2 or len(nums2) == 0:
            return self.findInSingle(nums1)
        total = len(nums1) + len(nums2)
        k = total // 2
        if total % 2 == 1:
            return findKthInTwoSortedArray(nums1=nums1, start1=0, nums2=nums2, start2=0, k=k + 1)
        else:
            first = findKthInTwoSortedArray(nums1=nums1, start1=0, nums2=nums2, start2=0, k=k)
            second = findKthInTwoSortedArray(nums1=nums1, start1=0, nums2=nums2, start2=0, k=k + 1)
            return (first + second) / 2

    # (long(m+n))   Use quick select # TODO fix
    def findMedianSortedArraysQuickSelectToFix(self, nums1: List[int], nums2: List[int]) -> float:

        def findKthInTwoSortedArray(start1, end1, start2, end2, k):
            remaining1 = end1 - start1 + 1
            remaining2 = end2 - start2 + 1
            if remaining1 == 0:
                return nums2[start2 + k - 1]
            if remaining2 == 0:
                return nums1[start1 + k - 1]
            if k == 1:
                return min(nums1[start1], nums2[start2])
            mid1 = start1 + (end1 - start1) // 2
            mid2 = start2 + (end2 - start2) // 2
            half = (remaining1 + remaining2) // 2 + 1
            if half >= k:
                if nums1[mid1] >= nums2[mid2]:
                    return findKthInTwoSortedArray(start1=start1, end1=(mid1 - 1), start2=start2, end2=end2, k=k)
                else:
                    return findKthInTwoSortedArray(start1=start1, end1=end1, start2=start2, end2=(mid2 - 1), k=k)
            else:
                if nums1[mid1] >= nums2[mid2]:
                    return findKthInTwoSortedArray(start1=start1, end1=end1, start2=(mid2 + 1), end2=end2, k=(k - (remaining2 / 2 + 1)))
                else:
                    return findKthInTwoSortedArray(start1=(mid1 + 1), end1=end1, start2=start2, end2=end2, k=(k - (remaining1 / 2 + 1)))

        # Edge cases
        if (not nums1 and not nums2) or (len(nums1)==0 and len(nums2)==0):
            return 0
        if not nums1 or len(nums1) == 0:
            return self.findInSingle(nums2)
        if not nums2 or len(nums2) == 0:
            return self.findInSingle(nums1)
        total = len(nums1) + len(nums2)
        k = total // 2
        if total % 2 == 1:
            return findKthInTwoSortedArray(start1=0, end1=len(nums1) - 1, start2=0, end2=len(nums2) - 1, k=k + 1)
        else:
            first = findKthInTwoSortedArray(start1=0, end1=len(nums1) - 1, start2=0, end2=len(nums2) - 1, k=k)
            second = findKthInTwoSortedArray(start1=0, end1=len(nums1) - 1, start2=0, end2=len(nums2) - 1, k=k + 1)
            return (first + second) / 2


    # O(log(min(m, n))). Log(length of smaller array)
    def findMedianSortedArraysBinarySearch(self, nums1: List[int], nums2: List[int]) -> float:
        # Edge cases
        if (not nums1 and not nums2) or (len(nums1)==0 and len(nums2)==0):
            return 0
        if not nums1 or len(nums1) == 0:
            return self.findInSingle(nums2)
        if not nums2 or len(nums2) == 0:
            return self.findInSingle(nums1)
        if len(nums1) <= len(nums2):
            return self.findInDouble(nums1, nums2)
        else:
            return self.findInDouble(nums2, nums1)
    
    def findInDouble(self, shorter: List[int], longer: List[int]) -> float:
        # Binary search on shorter array
        sLen, lLen = len(shorter), len(longer)
        low, high = 0, len(shorter)
        while low <= high:          # Use <= even high is len (not len - 1). It's used to set max value to inf
            partitionShort = low + (high - low) // 2        # Find partition point on shorter
            partitionLong = (sLen + lLen + 1) // 2 - partitionShort     # Find partition point on longer

            # Find min / max value on each partition
            maxLeftShort = -math.inf if partitionShort == 0 else shorter[partitionShort - 1]
            minRightShort = math.inf if partitionShort == sLen else shorter[partitionShort]

            maxLeftLong = -math.inf if partitionLong == 0 else longer[partitionLong - 1]
            minRightLong = math.inf if partitionLong == lLen else longer[partitionLong]

            # Find valid partion
            if maxLeftShort <= minRightLong and minRightShort >= maxLeftLong:
                if (sLen + lLen) % 2 == 0:
                    return (max(maxLeftShort, maxLeftLong) + min(minRightShort, minRightLong)) / 2
                else:
                    return max(maxLeftShort, maxLeftLong)
            elif maxLeftShort > minRightLong:
                high = partitionShort - 1
            else:
                low = partitionShort + 1
        raise ValueError("Arrays are not correctly sorted.")
    
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