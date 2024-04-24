from typing import List
from typing import Deque
from sortedcontainers import SortedList

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

    # Deque as monotonic queue to store index
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        n = len(nums)
        queue = Deque()
        ret = []
        for i, num in enumerate(nums):
            while queue and num > nums[queue[-1]]:  # Remove smaller elements index from tail
                queue.pop()
            while queue and (i - queue[0] >= k):    # Remove out of range index from head
                queue.popleft()
            queue.append(i)
            if i >= (k - 1) and queue:
                ret.append(nums[queue[0]])
        return ret

    def maxSlidingWindowSortedList(self, nums: List[int], k: int) -> List[int]:
        res = []
        sortedList = SortedList()
        for i in range(k - 1):
            sortedList.add(nums[i])
        left = 0
        for i in range(k - 1, len(nums)):
            sortedList.add(nums[i])
            res.append(sortedList[-1])
            sortedList.remove(nums[left])
            left += 1
        return res

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
        self.assertEqual(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3), [3,3,5,5,6,7])
        self.assertEqual(s.maxSlidingWindow([1],1), [1])



if __name__ == '__main__':
    unittest.main()