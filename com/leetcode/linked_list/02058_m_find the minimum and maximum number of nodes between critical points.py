from typing import List,Optional
import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        criticals = []
        prev = head
        cur = head.next
        index = 1
        while cur and cur.next:
            if (cur.val > prev.val and cur.val > cur.next.val) or (cur.val < prev.val and cur.val < cur.next.val):
                criticals.append(index)
            index += 1
            prev = cur
            cur = cur.next
        res = [-1, -1]
        if len(criticals) < 2:
            return res
        res[1] = (criticals[-1] - criticals[0])
        minDist = math.inf
        for i in range(1, len(criticals)):
            minDist = min(minDist, (criticals[i] - criticals[i - 1]))
        res[0] = minDist
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testMiddleNode(self):
        s = Solution()
        self.assertEqual(s.middleNode(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,None)))))).val, 3)
        self.assertEqual(s.middleNode(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6,None))))))).val, 4)


if __name__ == '__main__':
    unittest.main()