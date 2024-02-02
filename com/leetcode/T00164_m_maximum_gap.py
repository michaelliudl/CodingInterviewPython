from typing import List,Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    # def __eq__(self, __value: object) -> bool:
    #     return isinstance(__value, ListNode) and self.val == __value.val and self.next == __value.next

class Solution:

    # Same as sort
    def maximumGap(self, nums: List[int]) -> int:
        if not nums or len(nums) < 2: return 0
        heapq.heapify(nums)
        prev, maxGap = None, 0
        while nums:
            cur = heapq.heappop(nums)
            if prev:
                maxGap = max(maxGap, (cur - prev))
            prev = cur
        return maxGap

import unittest

class TestSolution(unittest.TestCase):
    def testMaximumGap(self):
        s = Solution()
        self.assertEqual(s.maximumGap(nums = [3,6,9,1]), 3)
        self.assertEqual(s.maximumGap(nums = [100,3,2,1]), 97)


if __name__ == '__main__':
    unittest.main()