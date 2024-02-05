from typing import List,Optional
import heapq

class ListNode:

    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return []
        cache={}
        for i in range(len(lists)):
            node=lists[i]
            while node:
                cache[(node.val, i)] = node
                node=node.next
        dummy=ListNode(val=float('inf'))
        cur=dummy
        heap=[]
        for i in range(len(lists)):
            node = lists[i]
            heapq.heappush(heap, (node.val, i))
        while heap:
            val, index = heapq.heappop(heap)
            node = cache[(val, index)]
            cur.next = node
            cur = node
            if node.next:
                heapq.heappush(heap, (node.next.val, index))
        return dummy.next


import unittest

class TestSolution(unittest.TestCase):
    def testMergeKLists(self):
        s = Solution()
        self.assertEqual(s.mergeKLists(lists = [
            ListNode(1,ListNode(4, ListNode(5))),
            ListNode(1,ListNode(3, ListNode(4))),
            ListNode(2,ListNode(6)),
        ]), 1)


if __name__ == '__main__':
    unittest.main()