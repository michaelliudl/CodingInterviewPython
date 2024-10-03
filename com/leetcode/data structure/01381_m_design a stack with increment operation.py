from typing import Optional,List,Deque

class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

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