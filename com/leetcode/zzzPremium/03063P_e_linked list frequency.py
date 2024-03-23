from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
Given the head of a linked list containing k distinct elements, return the head to a linked list of length k containing the 
frequency
 of each distinct element in the given linked list in any order.

'''

class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        pointer = head
        counts = {}
        while pointer:
            counts[pointer.val] = counts.get(pointer.val, 0) + 1
            pointer = pointer.next
        dummy = ListNode(-1)
        pointer = dummy
        for _, freq in counts.items():
            cur = ListNode(freq)
            pointer.next = cur
            pointer = cur
        return dummy.next
    
import unittest

class TestSolution(unittest.TestCase):
    def testFrequenciesOfElements(self):
        s = Solution()
        self.assertEqual(s.frequenciesOfElements(nums = [0,1,3,50,75], lower = 0, upper = 99), [[2,2],[4,49],[51,74],[76,99]])
        self.assertEqual(s.frequenciesOfElements(nums = [-1], lower = -1, upper = -1), [])


if __name__ == '__main__':
    unittest.main()
