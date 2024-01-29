from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return head
        slow,fast,secHead=head,head,None
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        secHead=slow.next
        slow.next=None

        prev,cur=None,secHead
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        secHead=prev

        p,q=head,secHead
        while p and q:
            tempP,tempQ=p.next,q.next
            p.next=q
            q.next=tempP
            p=tempP
            q=tempQ
        return





import unittest

class TestSolution(unittest.TestCase):
    def testReorderList(self):
        s = Solution()
        s.reorderList(ListNode(1,ListNode(2,ListNode(3,ListNode(4)))))
        s.reorderList(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5))))))
        
if __name__ == '__main__':
    unittest.main()