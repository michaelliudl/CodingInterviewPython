from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        

import unittest

class TestSolution(unittest.TestCase):
    def testOddEvenList(self):
        s = Solution()
        self.assertEqual(s.oddEvenList(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,None)))))), 
                         ListNode(1,ListNode(3,ListNode(5,ListNode(2,ListNode(4,None))))))
        self.assertEqual(s.oddEvenList(ListNode(2,ListNode(1,ListNode(3,ListNode(5,ListNode(6,ListNode(4,ListNode(7,None)))))))), 
                         ListNode(2,ListNode(3,ListNode(6,ListNode(7,ListNode(1,ListNode(5,ListNode(4,None))))))))
        self.assertEqual(s.oddEvenList(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6,None))))))), 
                         ListNode(1,ListNode(3,ListNode(5,ListNode(2,ListNode(4,ListNode(6,None)))))))

if __name__ == '__main__':
    unittest.main()