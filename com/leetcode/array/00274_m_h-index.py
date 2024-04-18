from typing import List

class MyCircularQueue:

    def __init__(self, k: int):
        self.cap = k
        self.queue = [-1] * k
        self.size = 0
        self.front = 0
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.cap
        self.queue[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.front] = -1
        self.front = (self.front + 1) % self.cap
        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.front]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
class Solution:
    pass


import unittest

class TestSolution(unittest.TestCase):

    def testMyCircularQueue(self):
        cq = MyCircularQueue(k=3)
        self.assertEqual(cq.enQueue(value=1), True)
        self.assertEqual(cq.enQueue(value=2), True)
        self.assertEqual(cq.enQueue(value=3), True)
        self.assertEqual(cq.enQueue(value=4), False)
        self.assertEqual(cq.Rear(), 3)
        self.assertEqual(cq.isFull(), True)
        self.assertEqual(cq.deQueue(), True)
        self.assertEqual(cq.enQueue(value=4), True)
        self.assertEqual(cq.Rear(), 4)
        
if __name__ == '__main__':
    unittest.main()