from typing import List

'''
You are asked to design a file system that allows you to create new paths and associate them with different values.

The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string "" and "/" are not.

Implement the FileSystem class:

bool createPath(string path, int value) Creates a new path and associates a value to it if possible and returns true. Returns false if the path already exists or its parent path doesn't exist.
int get(string path) Returns the value associated with path or returns -1 if the path doesn't exist.
'''
class FileSystem:

    def __init__(self):
        self.fileSys = {}

    def createPath(self, path: str, value: int) -> bool:
        node = self.fileSys
        elems = path[1:].split('/')
        for index, elem in enumerate(elems):
            if index == len(elems) - 1:
                if elem in node:
                    return False
                else:
                    node[elem] = (value, {})
                    return True
            if elem not in node:
                return False
            node = node[elem][1]

    def get(self, path: str) -> int:
        elems = path[1:].split('/')
        node = self.fileSys
        for index, elem in enumerate(elems):
            if index == len(elems) - 1 and elem in node:
                return node[elem][0]
            if elem not in node:
                return -1
            node = node[elem][1]
        return -1
class Solution:
    pass


import unittest

class TestSolution(unittest.TestCase):
    def testFileSystem(self):
        f = FileSystem()
        self.assertEqual(f.createPath("/a",1), True)
        self.assertEqual(f.get("/a"), 1)

    def testFileSystem1(self):
        f = FileSystem()
        self.assertEqual(f.createPath("/leet",1), True)
        self.assertEqual(f.createPath("/leet/code",2), True)
        self.assertEqual(f.get("/leet/code"), 2)
        self.assertEqual(f.createPath("/c/d",1), False)
        self.assertEqual(f.get("/c"), -1)

if __name__ == '__main__':
    unittest.main()