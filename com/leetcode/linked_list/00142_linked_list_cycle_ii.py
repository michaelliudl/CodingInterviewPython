from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    # def __eq__(self, __value: object) -> bool:
    #     return isinstance(__value, ListNode) and self.val == __value.val and self.next == __value.next

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        dh=ListNode(-1,head)
        s,f,d1,d2=dh,dh,dh,None
        while s and f and f.next:
            if s!=dh and s==f:
                d2=s
                break
            s=s.next
            f=f.next.next
        if not d2:
            return None
        while d1!=d2:
            d1=d1.next
            d2=d2.next
        return d1

import unittest

class TestSolution(unittest.TestCase):
    def testDetectCycle(self):
        s = Solution()
        self.assertEqual(s.detectCycle(ListNode(1,ListNode(2,None))).val, False)


if __name__ == '__main__':
    unittest.main()