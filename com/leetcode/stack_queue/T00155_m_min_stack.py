from typing import List

class MinStack:

    def __init__(self):
        self.stack=[]
        self.minHash={}
        self.curMin=float('inf')
        self.size=0

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.curMin=min(self.curMin,val)
        self.size+=1
        self.minHash[(val,self.size)]=self.curMin

    def pop(self) -> None:
        popped=self.stack.pop()
        del self.minHash[(popped,self.size)]
        self.size-=1
        if self.stack and self.minHash:
            self.curMin=self.minHash[(self.stack[-1],self.size)]
        else:
            self.curMin=float('inf')

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return 0

    def getMin(self) -> int:
        return self.curMin
    
class Solution:
    pass


import unittest

class TestSolution(unittest.TestCase):
    def testMinStack(self):
        s = MinStack()
        s.push(-2)
        s.push(0)
        s.push(-3)
        self.assertEqual(s.getMin(), -3)
        s.pop()
        self.assertEqual(s.top(), 0)
        self.assertEqual(s.getMin(), -2)
        s.pop()
        s.pop()
        self.assertEqual(s.getMin(), float('inf'))

    def testMinStack_1(self):
        s = MinStack()
        s.push(2)
        s.push(0)
        s.push(3)
        s.push(0)
        self.assertEqual(s.getMin(), 0)
        s.pop()
        self.assertEqual(s.getMin(), 0)
        s.pop()
        self.assertEqual(s.getMin(), 0)
        s.pop()
        self.assertEqual(s.getMin(), 2)



if __name__ == '__main__':
    unittest.main()