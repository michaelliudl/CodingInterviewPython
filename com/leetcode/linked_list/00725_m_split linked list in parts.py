from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # Get total list length, then use mod and rem of length over `k` to move cursor
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        listLen = 0
        cur = head
        while cur:
            listLen += 1
            cur = cur.next
        subLen = listLen // k
        rem = listLen % k
        cur = head
        res = []
        for _ in range(k):
            if not cur:
                res.append(None)
                continue
            res.append(cur)
            prev = None
            for _ in range(subLen):
                if not cur:
                    break
                prev = cur
                cur = cur.next
            if rem > 0:
                prev = cur
                cur = cur.next
                rem -= 1
            prev.next = None
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testHasCycle(self):
        s = Solution()
        self.assertEqual(s.hasCycle(ListNode(1,ListNode(2,None))), False)


if __name__ == '__main__':
    unittest.main()