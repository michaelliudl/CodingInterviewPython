from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, ListNode) and self.val == __value.val and self.next == __value.next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next or left<=0 or right<=0 or left>=right:
            return head
        dh=ListNode(-1,head)
        prev=dh
        for _ in range(left-1):
            prev=prev.next
        cur=prev.next
        for _ in range(left,right):
            t=prev.next
            prev.next=cur.next
            cur.next=cur.next.next
            prev.next.next=t
        return dh.next

import unittest

class TestSolution(unittest.TestCase):
    def testReverseBetween(self):
        s = Solution()
        self.assertEqual(s.reverseBetween(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,None))))),2,4), 
                         ListNode(1,ListNode(4,ListNode(3,ListNode(2,ListNode(5,None))))))
        self.assertEqual(s.reverseBetween(ListNode(3,ListNode(5,None)),2,2), ListNode(3,ListNode(5,None)))
        self.assertEqual(s.reverseBetween(ListNode(5,None),1,1), ListNode(5,None))

if __name__ == '__main__':
    unittest.main()