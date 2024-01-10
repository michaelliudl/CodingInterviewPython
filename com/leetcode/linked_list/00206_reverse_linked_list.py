from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, ListNode) and self.val == __value.val and self.next == __value.next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev,cur=None,head
        while cur is not None:
            t=cur.next
            cur.next=prev
            prev=cur
            cur=t
        return prev
    
    def reverseListRecur(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        return self.reverse(None,head)
    
    def reverse(self, prev: Optional[ListNode], cur: Optional[ListNode]) -> Optional[ListNode]:
        if not cur:
            return prev
        t=cur.next
        cur.next=prev
        return self.reverse(cur,t)

import unittest

class TestSolution(unittest.TestCase):
    def testReverseList(self):
        s = Solution()
        self.assertEqual(s.reverseList(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,None)))))), 
                         ListNode(5,ListNode(4,ListNode(3,ListNode(2,ListNode(1,None))))))
        self.assertEqual(s.reverseListRecur(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,None)))))), 
                         ListNode(5,ListNode(4,ListNode(3,ListNode(2,ListNode(1,None))))))

if __name__ == '__main__':
    unittest.main()