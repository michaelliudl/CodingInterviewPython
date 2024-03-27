from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

'''
You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.


'''

class Solution:

    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None
        nodeStack = []
        start = end = -1
        for index, char in enumerate(s):
            if char == '-' or '0' <= char <= '9':
                start = index if start < 0 else start
                end = index
            elif char == '(':
                if start >= 0 and end >= 0:
                    value = int(s[start:end + 1])
                    node = TreeNode(value)
                    nodeStack.append(node)
                    start = end = -1
            elif char == ')':
                child = None
                if start >= 0 and end >= 0:
                    value = int(s[start:end + 1])
                    child = TreeNode(value)
                    start = end = -1
                else:
                    if nodeStack:
                        child = nodeStack.pop()
                if nodeStack:
                    parent = nodeStack[-1]
                    if not parent.left:
                        parent.left = child
                    else:
                        parent.right = child
        if start >= 0 and end >= 0:
            value = int(s[start:end + 1])
            node = TreeNode(value)
            return node
        if nodeStack:
            return nodeStack[0]

import unittest

class TestSolution(unittest.TestCase):
    def testStr2tree(self):
        s = Solution()
        self.assertNotEqual(s.str2tree(s = "1(2(3(4(5(6(7(8)))))))(9(10(11(12(13(14(15)))))))"), None)
        self.assertNotEqual(s.str2tree(s = "4(2(3)(1))(6(5))"), None)
        self.assertNotEqual(s.str2tree(s = "4(2(3)(1))(6(5)(7))"), None)
        self.assertNotEqual(s.str2tree(s = "-4(2(3)(1))(6(5)(7))"), None)
        self.assertNotEqual(s.str2tree(s = "4"), None)


if __name__ == '__main__':
    unittest.main()