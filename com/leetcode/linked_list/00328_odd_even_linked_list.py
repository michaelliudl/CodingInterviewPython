from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, ListNode) and self.val == __value.val and self.next == __value.next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        odd,even,t=head,head.next,head.next
        while even and even.next:
            odd.next=even.next
            even.next=even.next.next
            odd.next.next=t
            odd=odd.next
            even=even.next
        return head

import unittest

class TestSolution(unittest.TestCase):
    def testOddEvenList(self):
        s = Solution()
        self.assertEqual(s.oddEvenList(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,None)))))), 
                         ListNode(1,ListNode(3,ListNode(5,ListNode(2,ListNode(4,None))))))
        self.assertEqual(s.oddEvenList(ListNode(2,ListNode(1,ListNode(3,ListNode(5,ListNode(6,ListNode(4,ListNode(7,None)))))))), 
                         ListNode(2,ListNode(3,ListNode(6,ListNode(7,ListNode(1,ListNode(5,ListNode(4,None))))))))
        self.assertEqual(s.oddEvenList(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6,None))))))), 
                         ListNode(1,ListNode(3,ListNode(5,ListNode(2,ListNode(4,ListNode(6,None)))))))

if __name__ == '__main__':
    unittest.main()