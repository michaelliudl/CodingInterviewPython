from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # Get total list length, then use mod and rem of length over `k` to move cursor
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        numSet = set(nums)
        while head and head.val in numSet:
            head = head.next
        cur = head
        while cur and cur.next:
            if cur.next.val in numSet:
                cur.next = cur.next.next
            else: cur = cur.next
        return head

import unittest

class TestSolution(unittest.TestCase):
    def testModifiedList(self):
        s = Solution()
        self.assertEqual(s.modifiedList(nums = [1,2,3], head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))), 
                         ListNode(4,ListNode(5)))
        self.assertEqual(s.modifiedList(nums = [1], head = ListNode(1,ListNode(2,ListNode(1,ListNode(2,ListNode(1,ListNode(2))))))), 
                         ListNode(1,ListNode(2,ListNode(2))))
        self.assertEqual(s.modifiedList(nums = [5], head = ListNode(1,ListNode(2,ListNode(3,ListNode(4))))), 
                         ListNode(1,ListNode(2,ListNode(3,ListNode(4)))))
        self.assertEqual(s.modifiedList(nums = [1,7,6,2,4], head = ListNode(3,ListNode(7,ListNode(1,ListNode(8,ListNode(1)))))), 
                         ListNode(3,ListNode(8)))


if __name__ == '__main__':
    unittest.main()