from typing import List
from typing import Deque


class Solution:

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return[]
        d={}
        st=[nums2[0]]
        for i in range(1,len(nums2)):
            v=nums2[i]
            while st and v>st[-1]:
                cur=st.pop()
                d[cur]=v
            st.append(v)
        return [-1 if n not in d else d[n] for n in nums1]

        

    def nextGreaterElementHash(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return[]
        r=[-1]*len(nums1)
        d={}
        for i,v in enumerate(nums2):
            d[v]=i
        for i,v in enumerate(nums1):
            for j in range(d[v]+1,len(nums2)):
                if nums2[j]>v:
                    r[i]=nums2[j]
                    break
        return r



import unittest

class TestSolution(unittest.TestCase):
    def testMaxSlidingWindow(self):
        s = Solution()
        self.assertEqual(s.maxSlidingWindowMonoToneQueue1([1,3,-1,-3,5,3,6,7],3), [3,3,5,5,6,7])
        self.assertEqual(s.maxSlidingWindowMonoToneQueue1([1],1), [1])



if __name__ == '__main__':
    unittest.main()