from typing import List,Optional
import heapq

class Solution:

    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        nextAvail = 0
        avails = []
        occupied = []   # (end, index)
        for i in range(len(times)):     # Add original index for matching with target
            times[i].append(i)
        times.sort(key=lambda time : time[0])   # Sort by earliest start
        for start, end, index in times:
            while occupied and occupied[0][0] <= start:
                nextEnd = heapq.heappop(occupied)[1]
                heapq.heappush(avails, nextEnd)
            if index == targetFriend:
                return avails[0] if avails else nextAvail
            if not avails:
                heapq.heappush(occupied, (end, nextAvail))
                nextAvail += 1
            else:
                avail = heapq.heappop(avails)
                heapq.heappush(occupied, (end, avail))

import unittest

class TestSolution(unittest.TestCase):
    def testMergeKLists(self):
        s = Solution()
        self.assertEqual(s.mergeKLists(lists = [
            ListNode(1,ListNode(2, ListNode(2))),
            ListNode(1,ListNode(1, ListNode(2)))
        ]).val, 1)
        self.assertEqual(s.mergeKLists(lists = [
            ListNode(1,ListNode(4, ListNode(5))),
            ListNode(1,ListNode(3, ListNode(4))),
            ListNode(2,ListNode(6)),
        ]).val, 1)
        self.assertEqual(s.mergeKLists(lists = []), None)
        self.assertEqual(s.mergeKLists(lists = [[]]), None)


if __name__ == '__main__':
    unittest.main()