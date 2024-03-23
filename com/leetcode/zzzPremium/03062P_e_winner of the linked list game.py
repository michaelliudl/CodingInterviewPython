from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
You are given the head of a linked list of even length containing integers.

Each odd-indexed node contains an odd integer and each even-indexed node contains an even integer.

We call each even-indexed node and its next node a pair, e.g., the nodes with indices 0 and 1 are a pair, the nodes with indices 2 and 3 are a pair, and so on.

For every pair, we compare the values of the nodes in the pair:

If the odd-indexed node is higher, the "Odd" team gets a point.
If the even-indexed node is higher, the "Even" team gets a point.
Return the name of the team with the higher points, if the points are equal, return "Tie".

'''

class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        if not head:
            return 'Tie'
        odd = even = 0
        pointer = head
        while pointer and pointer.next:
            if pointer.val > pointer.next.val:
                even += 1
            elif pointer.val < pointer.next.val:
                odd += 1
            pointer = pointer.next.next
        if odd == even:
            return 'Tie'
        return 'Odd' if odd > even else 'Even'
    
import unittest

class TestSolution(unittest.TestCase):
    def testFrequenciesOfElements(self):
        s = Solution()
        self.assertEqual(s.frequenciesOfElements(nums = [0,1,3,50,75], lower = 0, upper = 99), [[2,2],[4,49],[51,74],[76,99]])
        self.assertEqual(s.frequenciesOfElements(nums = [-1], lower = -1, upper = -1), [])


if __name__ == '__main__':
    unittest.main()
