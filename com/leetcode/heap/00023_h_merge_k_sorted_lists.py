from typing import List,Optional
import heapq

class ListNode:

    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

class MyListNode:
    def __init__(self, node=None):
        self.node=node
    
    def __lt__(self, other):
        return self.node.val <= other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        dummy=ListNode(val=float('inf'))
        cur=dummy
        heap=[]
        for i in range(len(lists)):
            node = lists[i]
            if node:
                heapq.heappush(heap, (node.val, MyListNode(node)))      # Need to wrap node with comparator
        while heap:
            val, myNode = heapq.heappop(heap)
            node = myNode.node
            cur.next = node
            cur = node
            if node.next:
                heapq.heappush(heap, (node.next.val, MyListNode(node.next)))
        return dummy.next


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