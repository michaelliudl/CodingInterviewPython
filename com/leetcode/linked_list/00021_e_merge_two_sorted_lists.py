from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    # def __eq__(self, __value: object) -> bool:
    #     return isinstance(__value, ListNode) and self.val == __value.val and self.next == __value.next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1
        dh=ListNode()
        cur = dh
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
                cur.next.next = list2
            else:
                cur.next = list2
                list2 = list2.next
                cur.next.next = list1
            cur = cur.next
        if list1: cur.next = list1
        if list2: cur.next = list2
        return dh.next

import unittest

class TestSolution(unittest.TestCase):
    def testMergeTwoLists(self):
        s = Solution()
        self.assertEqual(s.mergeTwoLists(list1 = ListNode(1,ListNode(2,ListNode(4))), list2=ListNode(1,ListNode(3,ListNode(4)))), False)


if __name__ == '__main__':
    unittest.main()