from typing import List
from typing import Deque

class MonoToneQueue:

    def __init__(self):
        self.dq=Deque()

    def monoPush(self, x:int):
        while self.dq and self.dq[-1]<x:
            self.dq.pop()
        self.dq.append(x)

    def monoPop(self, exited: int):
        if self.dq and exited>=self.dq[0]:
            self.dq.popleft()
    
    def front(self) -> int:
        return self.dq[0]

class Solution:

    def maxSlidingWindowMonoToneQueue(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return None
        if len(nums)<=k:
            return [max(nums)]
        r=list()
        mq=MonoToneQueue()
        for i in range(k):
            mq.monoPush(nums[i])
        r.append(mq.front())
        for i in range(k,len(nums)):
            mq.monoPush(nums[i])
            mq.monoPop(nums[i-k])
            r.append(mq.front())
        return r
    
    def maxSlidingWindowMonoToneQueue1(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return None
        r=[]
        mq=Deque()
        for i in range(len(nums)):
            while mq and nums[i]>nums[mq[-1]]:
                mq.pop()
            while mq and mq[0]<i-k+1:
                mq.popleft()
            mq.append(i)
            if i>=k-1:
                r.append(nums[mq[0]])
        return r

    def maxSlidingWindowBrute(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return None
        if len(nums)<=k:
            return [max(nums)]
        r=list()
        for i in range(len(nums)-k+1):
            r.append(max(nums[i:i+k]))
        return r

import unittest

class TestSolution(unittest.TestCase):
    def testMaxSlidingWindow(self):
        s = Solution()
        self.assertEqual(s.maxSlidingWindowMonoToneQueue1([1,3,-1,-3,5,3,6,7],3), [3,3,5,5,6,7])
        self.assertEqual(s.maxSlidingWindowMonoToneQueue1([1],1), [1])



if __name__ == '__main__':
    unittest.main()