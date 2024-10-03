from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1] * n for _ in range(m)]
        cur = head
        top, bottom, left, right = 0, m, 0, n
        while top < bottom and left < right and cur:
            for i in range(left, right):
                if not cur:
                    break
                res[top][i] = cur.val
                cur = cur.next
            top += 1
            for i in range(top, bottom):
                if not cur:
                    break
                res[i][right - 1] = cur.val
                cur = cur.next
            right -= 1
            if top < bottom:
                for i in range(right - 1, left - 1, -1):
                    if not cur:
                        break
                    res[bottom - 1][i] = cur.val
                    cur = cur.next
                bottom -= 1
            if left < right:
                for i in range(bottom - 1, top - 1, -1):
                    if not cur:
                        break
                    res[i][left] = cur.val
                    cur = cur.next
                left += 1
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testSpiralOrder(self):
        s = Solution()
        self.assertEqual(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]), [1,2,3,6,9,8,7,4,5])
        self.assertEqual(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]), [1,2,3,4,8,12,11,10,9,5,6,7])
        self.assertEqual(s.spiralOrder([[1,2,3]]), [1,2,3])

if __name__ == '__main__':
    unittest.main()