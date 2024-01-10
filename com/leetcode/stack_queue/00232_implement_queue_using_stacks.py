from typing import List

class MyQueue:

    def __init__(self):
        self.sst=list()
        self.qst=list()
        

    def push(self, x: int) -> None:
        while len(self.qst)>0:
            self.sst.append(self.qst.pop())
        self.qst.append(x)

    def pop(self) -> int:
        while len(self.sst)>0:
            self.qst.append(self.sst.pop())
        return self.qst.pop()

    def peek(self) -> int:
        while len(self.sst)>0:
            self.qst.append(self.sst.pop())
        if len(self.qst)==0:
            return -1
        return self.qst[len(self.qst)-1]

    def empty(self) -> bool:
        return len(self.sst)==0 and len(self.qst)==0


import unittest

class TestSolution(unittest.TestCase):
    def testMyQueue(self):
        s = MyQueue()
        s.push(1)
        s.push(2)
        self.assertEqual(s.peek(), 1)
        self.assertEqual(s.pop(), 1)
        self.assertEqual(s.empty(), False)



if __name__ == '__main__':
    unittest.main()