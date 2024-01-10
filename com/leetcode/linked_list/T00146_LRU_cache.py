from typing import List,Optional

class LRUCache:

    def __init__(self, capacity: int):
        

    def get(self, key: int) -> int:
        

    def put(self, key: int, value: int) -> None:

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