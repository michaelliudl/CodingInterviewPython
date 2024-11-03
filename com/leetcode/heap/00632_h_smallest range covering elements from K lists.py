from typing import List
import heapq

class Solution:

    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []   # Min heap of (element in sublist, sublist index in input, element index in sublist)
        # Init with (first element of sublist, original index of sublist, 0 = first element index)
        for index, num in enumerate(nums):
            heapq.heappush(heap, (num[0], index, 0))

        # Init boundaries with min/max values of first element in sublists
        left = min(num[0] for num in nums)
        right = max(num[0] for num in nums)
        res = [left, right]
        while heap:
            elem, subListIndex, elemIndex = heapq.heappop(heap)
            elemIndex += 1
            if elemIndex == len(nums[subListIndex]):    # Reach the end of one sublist
                return res
            nextElem = nums[subListIndex][elemIndex]    # Push next element in this sublist into heap
            heapq.heappush(heap, (nextElem, subListIndex, elemIndex))
            left = heap[0][0]
            right = max(right, nextElem)
            if (right - left) < (res[1] - res[0]):
                res = [left, right]


import unittest

class TestSolution(unittest.TestCase):
    def testFindMaximizedCapital(self):
        s = Solution()
        self.assertEqual(s.findMaximizedCapital(k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]), 4)
        self.assertEqual(s.findMaximizedCapital(k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]), 6)


if __name__ == '__main__':
    unittest.main()