from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, ListNode) and self.val == __value.val and self.next == __value.next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dh=ListNode(-1,head)
        p=dh
        while p.next and p.next.next:
            t1=p.next.next
            t2=p.next.next.next
            p.next.next.next=p.next
            p.next.next=t2
            p.next=t1
            p=t1.next
        return dh.next

import unittest

class TestSolution(unittest.TestCase):
    def testSwapPairs(self):
        s = Solution()
        self.assertEqual(s.swapPairs(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,None)))))), 
                         ListNode(2,ListNode(1,ListNode(4,ListNode(3,ListNode(5,None))))))
        self.assertEqual(s.swapPairs(ListNode(1,None)), ListNode(1,None))
        self.assertEqual(s.swapPairs(None), None)
        self.assertEqual(s.swapPairs(ListNode(1,ListNode(2,ListNode(3,ListNode(4,None))))), 
                         ListNode(2,ListNode(1,ListNode(4,ListNode(3,None)))))

if __name__ == '__main__':
    unittest.main()