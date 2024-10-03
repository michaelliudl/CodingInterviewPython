from typing import Optional,List,Deque

class MyCircularDeque:

    def __init__(self, k: int):
        self.cap = k
        self.deque = [-1] * k
        self.front = self.size = 0
        self.rear = k - 1

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front -= 1
        self.front = (self.front + self.cap) % self.cap
        self.deque[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear += 1
        self.rear %= self.cap
        self.deque[self.rear] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front += 1
        self.front %= self.cap
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear -= 1
        self.rear = (self.rear + self.cap) % self.cap
        self.size -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.deque[self.front]

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.deque[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

class Solution:
    pass

import unittest

class TestSolution(unittest.TestCase):

    def testAuthenticationManager(self):
        am = AuthenticationManager()
        am.mkdir('/m')
        self.assertEqual(am.ls('/m'), [])
        am.mkdir('/w')
        self.assertEqual(am.ls('/'), ['m','w'])
        self.assertEqual(am.ls('/w'), [])
        self.assertEqual(am.ls('/'), ['m','w'])
        am.addContentToFile('/dycete', 'emer')
        self.assertEqual(am.ls('/w'), [])
        self.assertEqual(am.ls('/'), ['dycete', 'm','w'])
        self.assertEqual(am.ls('/dycete'), ['dycete'])

    def testFileSystem3(self):
        fs = FileSystem()
        fs.mkdir('/zijzllb')
        self.assertEqual(fs.ls('/'), ['zijzllb'])
        self.assertEqual(fs.ls('/zijzllb'), [])
        fs.mkdir('/r')
        self.assertEqual(fs.ls('/'), ['r', 'zijzllb'])
        self.assertEqual(fs.ls('/r'), [])
        fs.addContentToFile('/zijzllb/hfktg', 'd')
        self.assertEqual(fs.readContentFromFile('/zijzllb/hfktg'), 'd')
        self.assertEqual(fs.ls('/'), ['r', 'zijzllb'])
        self.assertEqual(fs.readContentFromFile('/zijzllb/hfktg'), 'd')

    def testFileSystem1(self):
        fs = FileSystem()
        self.assertEqual(fs.ls('/'), [])
        fs.mkdir('/a/b/c')
        fs.addContentToFile('/a/b/c/d', 'hello')
        self.assertEqual(fs.ls('/'), ['a'])
        self.assertEqual(fs.readContentFromFile('/a/b/c/d'), 'hello')

    def testFileSystem2(self):
        fs = FileSystem()
        self.assertEqual(fs.ls('/'), [])
        fs.mkdir('/a/b/c')
        self.assertEqual(fs.ls('/a/b'), ['c'])

if __name__ == '__main__':
    unittest.main()