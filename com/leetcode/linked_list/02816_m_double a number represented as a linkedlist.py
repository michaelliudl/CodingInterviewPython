from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def getCarry(node):
            val = node.val * 2
            if node.next:
                val += getCarry(node.next)
            node.val = val % 10
            return val // 10
        
        if getCarry(head) == 1:
            return ListNode(1, head)
        return head

import unittest

class TestSolution(unittest.TestCase):
    def testReorderList(self):
        s = Solution()
        s.reorderList(ListNode(1,ListNode(2,ListNode(3,ListNode(4)))))
        s.reorderList(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5))))))
        
if __name__ == '__main__':
    unittest.main()