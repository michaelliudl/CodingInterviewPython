from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        if not list1:
            return list2
        if a > b:
            a, b = b, a
        dummy = ListNode(-float('inf'), list1)
        prevA  = prevB = dummy
        for i in range(b + 1):
            if i < a and prevA:
                prevA = prevA.next
            if prevB:
                prevB = prevB.next
        prevA.next = list2
        while prevA.next:
            prevA = prevA.next
        prevA.next = prevB.next
        prevB.next = None
        return dummy.next


import unittest

class TestSolution(unittest.TestCase):
    def testReorderList(self):
        s = Solution()
        s.reorderList(ListNode(1,ListNode(2,ListNode(3,ListNode(4)))))
        s.reorderList(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5))))))
        
if __name__ == '__main__':
    unittest.main()