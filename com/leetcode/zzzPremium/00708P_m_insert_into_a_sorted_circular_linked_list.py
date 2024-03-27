from typing import List, Optional

'''
Given a Circular Linked List node, which is sorted in non-descending order, write a function to insert a value insertVal into the list such that it remains a sorted circular list. The given node can be a reference to any single node in the list and may not necessarily be the smallest value in the circular list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the circular list should remain sorted.

If the list is empty (i.e., the given node is null), you should create a new single circular list and return the reference to that single node. Otherwise, you should return the originally given node.


'''

# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            head = Node(insertVal)
            head.next = head
            return head
        prev = head
        cur = head.next
        shouldInsert = False
        while True:
            if prev.val <= insertVal <= cur.val:    # Case 1. insert into non-descending sequence
                shouldInsert = True
            elif prev.val > cur.val:                # Case 2. between last largest node and first smallest node
                if insertVal >= prev.val or insertVal <= cur.val:   # Insert if greater than largest or smaller than smallest
                    shouldInsert = True
            if shouldInsert:
                node = Node(insertVal, cur)
                prev.next = node
                return head
            prev = cur
            cur = cur.next
            if prev == head:    # Back to starting point
                break
        node = Node(insertVal, cur)     # Case 3. insert right after head
        prev.next = node
        return head


import unittest

class TestSolution(unittest.TestCase):
    # Case 1
    def testInsert1(self):
        s = Solution()
        last = Node(1)
        head = Node(3,Node(4,last))
        last.next = head
        s.insert(head, 2)
        self.assertEqual(head.next.next.next.val, 2)

    # Base case
    def testInsert2(self):
        s = Solution()
        head = None
        head = s.insert(head, 1)
        self.assertEqual(head.val, 1)

    # Case 3
    def testInsert3(self):
        s = Solution()
        head = Node(1)
        head.next = head
        s.insert(head, 0)
        self.assertEqual(head.next.val, 0)

    # Case 2, small
    def testInsert4(self):
        s = Solution()
        last = Node(1)
        head = Node(3,Node(5,last))
        last.next = head
        s.insert(head, 0)
        self.assertEqual(head.next.next.val, 0)

    # Case 3, small, insert before head
    def testInsert5(self):
        s = Solution()
        last = Node(5)
        head = Node(1,Node(3,last))
        last.next = head
        s.insert(head, 0)
        self.assertEqual(head.next.next.next.val, 0)

    # Case 2
    def testInsert6(self):
        s = Solution()
        last = Node(5)
        head = Node(1,Node(3,last))
        last.next = head
        s.insert(head, 2)
        self.assertEqual(head.next.val, 2)

    # Case 3, equal to head
    def testInsert7(self):
        s = Solution()
        last = Node(3)
        head = Node(3,Node(5,Node(6,last)))
        last.next = head
        s.insert(head, 3)
        self.assertEqual(head.next.val, 3)
        self.assertEqual(head.next.next.next.next.val, 3)

    # Case 2, large, insert right after head
    def testInsert8(self):
        s = Solution()
        last = Node(3)
        head = Node(3,Node(1,last))
        last.next = head
        s.insert(head, 4)
        self.assertEqual(head.next.val, 4)


if __name__ == '__main__':
    unittest.main()