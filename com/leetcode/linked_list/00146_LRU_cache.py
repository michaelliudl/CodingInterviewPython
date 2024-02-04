from typing import List,Optional

class ListNode:

    def __init__(self, key=0, val=0, prev=None, next=None) -> None:
        self.key=key
        self.val=val
        self.prev=prev
        self.next=next

class LRUCache:

    def __init__(self, capacity: int):
        self.dummyHead=ListNode(key=-float('inf'),val=-float('inf'))
        self.dummyTail=ListNode(key=float('inf'),val=float('inf'))
        self.dummyHead.next=self.dummyTail
        self.dummyTail.prev=self.dummyHead
        self.map={}
        self.capacity=capacity
        self.size=0

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node=self.map[key]
        self._front(node)
        return node.val
    
    def _front(self, node):
        if node.next:
            node.next.prev=node.prev
        if node.prev:
            node.prev.next=node.next
        node.next=self.dummyHead.next
        node.prev=self.dummyHead
        node.next.prev=node
        node.prev.next=node


    def put(self, key: int, value: int) -> None:

        def _tryEvict():
            if self.size==self.capacity:
                tail=self.dummyTail.prev
                tail.prev.next=tail.next
                tail.next.prev=tail.prev
                del self.map[tail.key]
                self.size-=1

        node,addNew=None,False
        if key in self.map:
            node=self.map[key]
            node.val=value
        else:
            node=ListNode(key=key, val=value)
            addNew=True
            self.map[key]=node
        if addNew:
            _tryEvict()
            self.size+=1
        self._front(node)

import unittest

class TestSolution(unittest.TestCase):
    def testLRUCache(self):
        c = LRUCache(capacity=2)
        c.put(key=1,value=1)
        c.put(key=2,value=2)
        self.assertEqual(c.get(1), 1)
        c.put(key=3,value=3)
        self.assertEqual(c.get(2), -1)
        c.put(key=4,value=4)
        self.assertEqual(c.get(1), -1)
        self.assertEqual(c.get(3), 3)
        self.assertEqual(c.get(4), 4)

    def testLRUCache1(self):
        c = LRUCache(capacity=2)
        c.put(key=1,value=0)
        c.put(key=2,value=2)
        self.assertEqual(c.get(1), 0)
        c.put(key=3,value=3)
        self.assertEqual(c.get(2), -1)
        c.put(key=4,value=4)
        self.assertEqual(c.get(1), -1)
        self.assertEqual(c.get(3), 3)
        self.assertEqual(c.get(4), 4)

    def testLRUCache2(self):
        c = LRUCache(capacity=2)
        c.put(key=2,value=1)
        c.put(key=1,value=1)
        c.put(key=2,value=3)
        c.put(key=4,value=1)
        self.assertEqual(c.get(1), -1)
        self.assertEqual(c.get(2), 3)
        

if __name__ == '__main__':
    unittest.main()