from typing import List

class MyStack:

    def __init__(self):
        self.qst=list()

    def push(self, x: int) -> None:
        self.qst.append(x)

    def pop(self) -> int:
        return self.qst.pop()

    def top(self) -> int:
        if len(self.qst)>0:
            return self.qst[len(self.qst)-1]
        return -1

    def empty(self) -> bool:
        return len(self.qst)==0

import unittest

class TestSolution(unittest.TestCase):
    def testMyStack(self):
        s = MyStack()
        s.push(1)
        s.push(2)
        self.assertEqual(s.top(), 2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.empty(), False)



if __name__ == '__main__':
    unittest.main()