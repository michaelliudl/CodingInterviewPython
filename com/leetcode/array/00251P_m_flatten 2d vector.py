from typing import List

'''
Design an iterator to flatten a 2D vector. It should support the next and hasNext operations.

Implement the Vector2D class:

Vector2D(int[][] vec) initializes the object with the 2D vector vec.
next() returns the next element from the 2D vector and moves the pointer one step forward. You may assume that all the calls to next are valid.
hasNext() returns true if there are still some elements in the vector, and false otherwise.
'''

class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.indexRow = 0
        self.indexCol = 0

    def next(self) -> int:
        if self.hasNext():
            value = self.vec[self.indexRow][self.indexCol]
            self.indexCol += 1
            return value

    def hasNext(self) -> bool:
        while self.indexRow < len(self.vec) and self.indexCol == len(self.vec[self.indexRow]):
            self.indexRow += 1
            self.indexCol = 0
        if self.indexRow == len(self.vec):
            return False
        if self.indexRow == len(self.vec) - 1 and self.indexCol == len(self.vec[-1]):
            return False
        return True

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()

class Solution:
    pass
        

import unittest

class TestSolution(unittest.TestCase):

    def testVector2D(self):
        v = Vector2D(vec=[[1, 2], [3], [4]])
        self.assertEqual(v.next(), 1)
        self.assertEqual(v.next(), 2)
        self.assertEqual(v.next(), 3)
        self.assertEqual(v.hasNext(), True)
        self.assertEqual(v.hasNext(), True)
        self.assertEqual(v.next(), 4)
        self.assertEqual(v.hasNext(), False)
    
    def testVector2D1(self):
        v = Vector2D(vec=[[], [3]])
        self.assertEqual(v.hasNext(), True)
        self.assertEqual(v.next(), 3)
        self.assertEqual(v.hasNext(), False)

if __name__ == '__main__':
    unittest.main()