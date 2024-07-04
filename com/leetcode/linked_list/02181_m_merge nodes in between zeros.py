from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        while head.val == 0:
            head = head.next
        prev = head
        cur = head.next
        while cur:
            if cur.val != 0:
                prev.val += cur.val
                cur = cur.next
            else:
                while cur and cur.val == 0:
                    cur = cur.next
                prev.next = cur
                prev = cur
                if cur:
                    cur = cur.next
        return head

import unittest

class TestSolution(unittest.TestCase):
    def testHasCycle(self):
        s = Solution()
        self.assertEqual(s.hasCycle(ListNode(1,ListNode(2,None))), False)


if __name__ == '__main__':
    unittest.main()