from typing import List

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        if not nums1 or not nums2 or not nums3 or not nums4:
            return 0
        d=dict()
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                s=nums1[i]+nums2[j]
                d[s]=d[s]+1 if s in d else 1
        n=0
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                s=0-(nums3[i]+nums4[j])
                n+=0 if not s in d else d[s]
        return n

import unittest

class TestSolution(unittest.TestCase):
    def testFourSumCount(self):
        s = Solution()
        self.assertEqual(s.fourSumCount(nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]), 2)
        self.assertEqual(s.fourSumCount(nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]), 1)


if __name__ == '__main__':
    unittest.main()