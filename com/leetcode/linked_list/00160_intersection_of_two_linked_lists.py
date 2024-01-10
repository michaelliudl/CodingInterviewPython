from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    # def __eq__(self, __value: object) -> bool:
    #     return isinstance(__value, ListNode) and self.val == __value.val and self.next == __value.next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        lenA,lenB=0,0
        pA,pB=headA,headB
        while pA:
            lenA+=1
            pA=pA.next
        while pB:
            lenB+=1
            pB=pB.next
        pA,pB=headA,headB
        if lenA>lenB:
            for i in range(lenA-lenB):
                pA=pA.next
        elif lenA<lenB:
            for i in range(lenB-lenA):
                pB=pB.next
        while pA and pB and (pA!=pB):
            pA=pA.next
            pB=pB.next
        if not pA or not pB:
            return None
        return pA

import unittest

class TestSolution(unittest.TestCase):
    def testGetIntersectionNode(self):
        s = Solution()
        inter1=ListNode(8,ListNode(4,ListNode(5,None)))
        self.assertEqual(s.getIntersectionNode(ListNode(4,ListNode(1,inter1)),
                                               ListNode(5,ListNode(6,ListNode(1,inter1)))), inter1)
        inter2=ListNode(2,ListNode(4,None))
        self.assertEqual(s.getIntersectionNode(ListNode(1,ListNode(9,ListNode(1,inter2))),
                                               ListNode(3,inter2)), inter2)
        self.assertEqual(s.getIntersectionNode(ListNode(2,ListNode(6,ListNode(4,None))),
                                               ListNode(1,ListNode(5,None))), None)
        inter3=ListNode(1,None)
        self.assertEqual(s.getIntersectionNode(inter3,inter3), inter3)

if __name__ == '__main__':
    unittest.main()