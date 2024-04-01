from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 0:
            return head
        dummy = ListNode(-1, head)
        reverseTail = head
        prev = None
        cur = head
        pointer = dummy
        prevGroupHead = dummy
        while pointer:
            for _ in range(k):
                if pointer:
                    pointer = pointer.next
            if not pointer:
                break
            prevGroupHead.next = pointer
            for _ in range(k):
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            reverseTail.next = cur
            pointer = prevGroupHead = reverseTail
            reverseTail = cur
            prev = None
        return dummy.next
        


import unittest

class TestSolution(unittest.TestCase):
    def testHasCycle(self):
        s = Solution()
        self.assertEqual(s.hasCycle(ListNode(1,ListNode(2,None))), False)


if __name__ == '__main__':
    unittest.main()