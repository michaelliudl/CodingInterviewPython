from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, ListNode) and self.val == __value.val and self.next == __value.next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or n<=0:
            return head
        dh=ListNode(-1,head)
        s,f,i=dh,dh,n
        while i>0 and f:
            f=f.next
            i-=1
        while f and f.next:
            f=f.next
            s=s.next
        s.next=s.next.next
        return dh.next

import unittest

class TestSolution(unittest.TestCase):
    def testRemoveNthFromEnd(self):
        s = Solution()
        self.assertEqual(s.removeNthFromEnd(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,None))))),2), 
                         ListNode(1,ListNode(2,ListNode(3,ListNode(5,None)))))
        self.assertEqual(s.removeNthFromEnd(ListNode(1,None),1), None)
        self.assertEqual(s.removeNthFromEnd(ListNode(1,ListNode(2,None)),1), 
                         ListNode(1,None))

if __name__ == '__main__':
    unittest.main()