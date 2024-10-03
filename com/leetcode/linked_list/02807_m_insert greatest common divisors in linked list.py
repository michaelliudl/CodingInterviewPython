from typing import List,Optional
import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        cur = head.next
        while cur:
            prev.next = ListNode(val=math.gcd(prev.val, cur.val), next=cur)
            prev = cur
            cur = cur.next
        return head


import unittest

class TestSolution(unittest.TestCase):
    def testCopyRandomList(self):
        s = Solution()
        pass
        
if __name__ == '__main__':
    unittest.main()