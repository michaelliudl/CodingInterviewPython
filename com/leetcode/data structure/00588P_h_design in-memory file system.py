from typing import Optional,List,Deque

'''
Design a data structure that simulates an in-memory file system.

Implement the FileSystem class:

FileSystem() Initializes the object of the system.
List<String> ls(String path)
If path is a file path, returns a list that only contains this file's name.
If path is a directory path, returns the list of file and directory names in this directory.
The answer should in lexicographic order.
void mkdir(String path) Makes a new directory according to the given path. The given directory path does not exist. If the middle directories in the path do not exist, you should create them as well.
void addContentToFile(String filePath, String content)
If filePath does not exist, creates that file containing given content.
If filePath already exists, appends the given content to original content.
String readContentFromFile(String filePath) Returns the content in the file at filePath.

'''

class Node:

    def __init__(self, name = None):
        self.name = name

class FileNode(Node):

    def __init__(self, name = None, content = None):
        super().__init__(name)
        self.content = content

class DirNode(Node):

    def __init__(self, name = None):
        super().__init__(name)
        self.files = {}
        self.children = {}

class FileSystem:

    def __init__(self):
        self.root = DirNode(name = '/')

    def ls(self, path: str) -> List[str]:
        node = self.root
        pathList = path.split('/')
        for i in range(1, len(pathList)):
            pathName = pathList[i]
            if pathName in node.files:
                node = node.files[pathName]
            elif pathName in node.children:
                node = node.children[pathName]
        result = []
        if node:
            if isinstance(node, FileNode):
                result.append(node.name)
            else:
                result.extend(list(node.files))
                result.extend(list(node.children.keys()))
                result.sort()
        return result

    def mkdir(self, path: str) -> None:
        node = self.root
        pathList = path.split('/')
        for i in range(1, len(pathList)):
            dirName = pathList[i]
            if dirName not in node.children:
                node.children[dirName] = DirNode(dirName)
            node = node.children[dirName]

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.root
        pathList = filePath.split('/')
        for i in range(1, len(pathList) - 1):
            dirName = pathList[i]
            if dirName not in node.children:
                node.children[dirName] = DirNode(dirName)
            node = node.children[dirName]
        if node:
            fileName = pathList[-1]
            if fileName in node.files:
                node.files[fileName].content += content
            else:
                fileNode = FileNode(fileName, content)
                node.files[fileName] = fileNode


    def readContentFromFile(self, filePath: str) -> str:
        node = self.root
        pathList = filePath.split('/')
        for i in range(1, len(pathList) - 1):
            dirName = pathList[i]
            if dirName in node.children:
                node = node.children[dirName]
        if node:
            fileName = pathList[-1]
            if fileName in node.files:
                return node.files[fileName].content
        return ''


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)

class Solution:
    pass

import unittest

class TestSolution(unittest.TestCase):

    def testFileSystem(self):
        fs = FileSystem()
        fs.mkdir('/m')
        self.assertEqual(fs.ls('/m'), [])
        fs.mkdir('/w')
        self.assertEqual(fs.ls('/'), ['m','w'])
        self.assertEqual(fs.ls('/w'), [])
        self.assertEqual(fs.ls('/'), ['m','w'])
        fs.addContentToFile('/dycete', 'emer')
        self.assertEqual(fs.ls('/w'), [])
        self.assertEqual(fs.ls('/'), ['dycete', 'm','w'])
        self.assertEqual(fs.ls('/dycete'), ['dycete'])

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