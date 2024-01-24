from typing import List
from typing import Deque


class Solution:

    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        r=[-1]*len(nums)
        st=[0]
        for i in range(1,2*len(nums)):
            cur=nums[i%len(nums)]
            while st and cur>nums[st[-1]%len(nums)]:
                j=st.pop()
                r[j%len(nums)]=cur
            st.append(i)
        return r

    def nextGreaterElementsCopy(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums2=nums+nums
        r=[-1]*len(nums)
        st=[(0,nums2[0])]
        for i in range(1,len(nums2)):
            v=nums2[i]
            while st and v>st[-1][1]:
                j,_=st.pop()
                if j>=len(nums):
                    continue
                r[j]=v
            st.append((i,v))
        return r



import unittest

class TestSolution(unittest.TestCase):
    def testMaxSlidingWindow(self):
        s = Solution()
        self.assertEqual(s.maxSlidingWindowMonoToneQueue1([1,3,-1,-3,5,3,6,7],3), [3,3,5,5,6,7])
        self.assertEqual(s.maxSlidingWindowMonoToneQueue1([1],1), [1])



if __name__ == '__main__':
    unittest.main()