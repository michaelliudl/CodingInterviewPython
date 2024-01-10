from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2 or len(nums1)==0 or len(nums2)==0:
            return list
        return list(set(nums1).intersection(set(nums2)))

import unittest

class TestSolution(unittest.TestCase):
    def testIntersection(self):
        s = Solution()
        self.assertEqual(s.intersection(nums1 = [1,2,2,1], nums2 = [2,2]), [2])
        self.assertEqual(s.intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4]), [9,4])


if __name__ == '__main__':
    unittest.main()