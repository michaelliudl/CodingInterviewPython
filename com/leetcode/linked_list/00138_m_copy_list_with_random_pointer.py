from typing import List,Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        map = {}
        newDummy = Node(-1)
        node, newNode = head, newDummy
        while node:
            newNode.next = Node(node.val)
            map[node] = newNode.next
            node = node.next
            newNode = newNode.next
        node = head
        while node:
            if node.random:
                map[node].random = map[node.random]
            node = node.next
        return newDummy.next





import unittest

class TestSolution(unittest.TestCase):
    def testCopyRandomList(self):
        s = Solution()
        pass
        
if __name__ == '__main__':
    unittest.main()