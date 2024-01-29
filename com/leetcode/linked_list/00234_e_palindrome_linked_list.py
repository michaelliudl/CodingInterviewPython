from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def reverse():
            prev,cur=None,secHead
            while cur:
                temp=cur.next
                cur.next=prev
                prev=cur
                cur=temp
            return prev

        def findSecHead():
            nonlocal size
            slow,fast=dummy,dummy
            while fast and fast.next and fast.next.next:
                slow=slow.next
                fast=fast.next.next
            if size%2==0:
                secHead=slow.next
                slow.next=None
                return secHead
            else:
                secHead=slow.next.next
                slow.next.next=None
                slow.next=None
                return secHead

        def getSize():
            size=0
            p=head
            while p:
                size+=1
                p=p.next
            return size

        if not head: return False
        if not head.next: return True
        dummy=ListNode(val=-1,next=head)
        size=getSize()
        secHead=findSecHead()
        secHead=reverse()
        p,q=head,secHead
        while p and q:
            if p.val!=q.val:
                return False
            p=p.next
            q=q.next
        if p or q:
            return False
        return True



import unittest

class TestSolution(unittest.TestCase):
    def testIsPalindrome(self):
        s = Solution()
        self.assertEqual(s.isPalindrome(ListNode(1)), True)
        self.assertEqual(s.isPalindrome(ListNode(1,ListNode(2,ListNode(2,ListNode(1))))), True)
        self.assertEqual(s.isPalindrome(ListNode(1,ListNode(2,ListNode(3,ListNode(2,ListNode(1)))))), True)
        self.assertEqual(s.isPalindrome(ListNode(1,ListNode(2,ListNode(3,ListNode(3,ListNode(2,ListNode(1))))))), True)
        self.assertEqual(s.isPalindrome(ListNode(1,ListNode(2))), False)

if __name__ == '__main__':
    unittest.main()