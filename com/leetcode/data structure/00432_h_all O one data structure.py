from typing import Optional, List, Deque

class Node:

    def __init__(self, count=0, key=None):
        self.count = count
        self.keys = {key} if key else set()
        self.prev = self.next = None

# Similar to 460 LFU cache
# Map of string -> Node
# Double linked list Node for different count of string and set of strings with same count
class AllOne:

    def __init__(self):
        self.keyNode = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        if key in self.keyNode:
            self._incrExistingKey(key)
        else:
            self._addKey(key)

    def dec(self, key: str) -> None:
        self._decrKey(key)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ''
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ''
        return next(iter(self.head.next.keys))
    
    def _addKey(self, key):
        if self.head.next.count == 1:
            self.head.next.keys.add(key)
        else:
            self._addAfter(self.head, Node(count=1, key=key))
        self.keyNode[key] = self.head.next
    
    def _incrExistingKey(self, key):
        node = self.keyNode[key]
        node.keys.remove(key)
        if node.next == self.tail or node.next.count > node.count + 1:
            self._addAfter(node, Node(count=(node.count + 1)))
        node.next.keys.add(key)
        self.keyNode[key] = node.next
        if not node.keys:
            self._remove(node)
    
    def _decrKey(self, key):
        node = self.keyNode[key]
        node.keys.remove(key)
        if node.count > 1:
            if node.prev == self.head or node.prev.count != node.count - 1:
                self._addAfter(node.prev, Node(count=(node.count - 1)))
            node.prev.keys.add(key)
            self.keyNode[key] = node.prev
        else:
            del self.keyNode[key]
        if not node.keys:
            self._remove(node)

    def _addAfter(self, node, newNode):
        newNode.prev = node
        newNode.next = node.next
        node.next.prev = newNode
        node.next = newNode
    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

class Solution:
    pass

import unittest

class TestSolution(unittest.TestCase):

    def testAllOne(self):
        allOne = AllOne()
        allOne.inc('hello')
        allOne.inc('hello')
        self.assertEqual(allOne.getMaxKey(), 'hello')
        self.assertEqual(allOne.getMinKey(), 'hello')
        allOne.inc('leet')
        self.assertEqual(allOne.getMaxKey(), 'hello')
        self.assertEqual(allOne.getMinKey(), 'leet')


if __name__ == '__main__':
    unittest.main()