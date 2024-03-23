from typing import List
import heapq
from sortedcontainers import SortedList

class Solution:

    # Use BBST to maintain k sorted elements, O((n-k)*logk)
    # Python SortedList doesn't support get by index other than 0 and -1. Need to use 2 SortedLists to replace 2 heaps and reduce window update time to O(k)
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

        def median():
            if k & 1:
                return lowSL[-1]
            else:
                return (lowSL[-1] + highSL[0]) / 2

        if not nums or k <= 0:
            return []
        n = len(nums)
        k = k if k < n else n
        lowSL, highSL = SortedList(), SortedList()
        result = [None] * (n - k + 1)
        for i in range(n):
            if i >= k:
                winOut = nums[i - k]
                if winOut <= lowSL[-1]:
                    lowSL.remove(winOut)
                else:
                    highSL.remove(winOut)
            highSL.add(nums[i])
            while (highSL and lowSL and highSL[0] < lowSL[-1]) or len(highSL) > len(lowSL):
                lowSL.add(highSL.pop(0))
            while len(lowSL) - len(highSL) > 1:
                highSL.add(lowSL.pop())
            if i >= k - 1:
                result[i - k + 1] = median()
        return result

    # W/O BBST, use two heaps. Time out: O((n-k)*(k*logk))
    def medianSlidingWindow1(self, nums: List[int], k: int) -> List[float]:

        def median():
            if len(lowHeap) == len(highHeap):
                return (highHeap[0] - lowHeap[0]) / 2
            else:
                return -lowHeap[0]
        
        def outOnLow(winOut):
            lowHeap.remove(-winOut)
            heapq.heapify(lowHeap)
            # temp = []
            # while lowHeap and winOut < -lowHeap[0]:
            #     temp.append(heapq.heappop(lowHeap))
            # if lowHeap:
            #     heapq.heappop(lowHeap)
            # for t in temp:
            #     heapq.heappush(lowHeap, t)
        
        def outOnHigh(winOut):
            highHeap.remove(winOut)
            heapq.heapify(highHeap)
            # temp = []
            # while highHeap and winOut > highHeap[0]:
            #     temp.append(heapq.heappop(highHeap))
            # if highHeap:
            #     heapq.heappop(highHeap)
            # for t in temp:
            #     heapq.heappush(highHeap, t)
        
        def maintain(winOut, winIn):
            if winOut <= -lowHeap[0]:
                outOnLow(winOut)
            else:
                outOnHigh(winOut)
            heapq.heappush(highHeap, winIn)
            while (highHeap and lowHeap and highHeap[0] < -lowHeap[0]) or len(highHeap) > len(lowHeap):
                heapq.heappush(lowHeap, -heapq.heappop(highHeap))
            while len(lowHeap) - len(highHeap) > 1:
                heapq.heappush(highHeap, -heapq.heappop(lowHeap))

        if not nums or k <= 0:
            return []
        n = len(nums)
        if k >= n:
            k = n
        result = [-float('inf')] * (n - k + 1)
        lowHeap, highHeap = [], []
        for i in range(k):
            heapq.heappush(highHeap, nums[i])
        while len(highHeap) > len(lowHeap):
            heapq.heappush(lowHeap, -heapq.heappop(highHeap))
        result[0] = median()
        for i in range(k, n):
            maintain(nums[i - k], nums[i])
            result[i - k + 1] = median()
        return result


import unittest

class TestSolution(unittest.TestCase):
    def testMedianSlidingWindow(self):
        s = Solution()
        self.assertEqual(s.medianSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3), [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000])
        self.assertEqual(s.medianSlidingWindow(nums = [1,2,3,4,2,3,1,4,2], k = 3), [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000])


if __name__ == '__main__':
    unittest.main()