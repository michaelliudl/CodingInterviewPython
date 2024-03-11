from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    # def __eq__(self, __value: object) -> bool:
    #     return isinstance(__value, ListNode) and self.val == __value.val and self.next == __value.next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        dh=ListNode(-1,head)
        s,f=dh,dh
        while f and f.next:
            f=f.next.next
            s=s.next
        if not f:
            return s
        if not f.next:
            return s.next
        return None

import unittest

class TestSolution(unittest.TestCase):
    def testMiddleNode(self):
        s = Solution()
        self.assertEqual(s.middleNode(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,None)))))).val, 3)
        self.assertEqual(s.middleNode(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6,None))))))).val, 4)


if __name__ == '__main__':
    unittest.main()