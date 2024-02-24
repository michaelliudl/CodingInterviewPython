import random
from typing import List

class RandomizedSet:

    def __init__(self):
        self.map={}
        self.arr=[]
        self.length=0
        self.cap=0

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        if self.length == self.cap:
            self.arr.append(val)
            self.length += 1
            self.cap += 1
        else:
            self.arr[self.length] = val
            self.length += 1
        self.map[val] = self.length - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        valPos = self.map[val]
        del self.map[val]
        if valPos < self.length - 1:
            newVal = self.arr[self.length - 1]
            self.arr[valPos] = newVal
            self.map[newVal] = valPos
        self.length -= 1
        return True

    def getRandom(self) -> int:
        return self.arr[random.randint(0, self.length - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

class Solution:

        pass

import unittest

class TestSolution(unittest.TestCase):

    def testRandomizedSet(self):
        rs = RandomizedSet()
        self.assertEqual(rs.remove(0), False)
        self.assertEqual(rs.remove(0), False)
        self.assertEqual(rs.insert(0), True)
        self.assertIn(rs.getRandom(), (0,1))
        self.assertEqual(rs.remove(0), True)
        self.assertEqual(rs.insert(0), True)

    def testRandomizedSet1(self):
        rs = RandomizedSet()
        self.assertEqual(rs.insert(1), True)
        self.assertEqual(rs.remove(2), False)
        self.assertEqual(rs.insert(2), True)
        self.assertIn(rs.getRandom(), (1,2))
        self.assertEqual(rs.remove(1), True)
        self.assertEqual(rs.insert(2), False)
        self.assertIn(rs.getRandom(), (1,2))


if __name__ == '__main__':
    unittest.main()