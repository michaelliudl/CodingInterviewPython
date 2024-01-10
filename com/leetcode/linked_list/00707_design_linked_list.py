from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    # def __eq__(self, __value: object) -> bool:
    #     return isinstance(__value, ListNode) and self.val == __value.val and self.next == __value.next

class MyLinkedList:

    def __init__(self):
        self.dh=ListNode(-1,None)
        self.size = 0

    def get(self, index: int) -> int:
        if index<0 or index>=self.size:
            return -1
        p=self.dh
        for _ in range(index):
            p=p.next
        return p.next.val

    def addAtHead(self, val: int) -> None:
        nn=ListNode(val, self.dh.next)
        self.dh.next=nn
        self.size+=1

    def addAtTail(self, val: int) -> None:
        nn=ListNode(val, None)
        p=self.dh
        while p.next:
            p=p.next
        p.next=nn
        self.size+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index<0 or index > self.size:
            return
        p=self.dh
        for _ in range(index):
            p=p.next
        nn=ListNode(val,p.next)
        p.next=nn
        self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>=self.size:
            return
        p=self.dh
        for _ in range(index):
            p=p.next
        p.next=p.next.next
        self.size-=1

import unittest

class TestSolution(unittest.TestCase):
    def testMyLinkedList(self):
        mll = MyLinkedList()
        mll.addAtHead(1)
        mll.addAtTail(3)
        mll.addAtIndex(1,2)
        self.assertEqual(mll.get(1), 2)
        mll.deleteAtIndex(1)
        self.assertEqual(mll.get(1), 3)


if __name__ == '__main__':
    unittest.main()