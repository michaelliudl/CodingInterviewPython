from typing import List

'''
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is below:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}

'''
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def getPath(node):
            path = []
            while node:
                path.append(node)
                node = node.parent
            return path

        if not p or not q:
            return None
        pathP = getPath(p)
        pathQ = getPath(q)
        indexP, indexQ = len(pathP) - 1, len(pathQ) - 1
        while indexP >= 0 and indexQ >= 0:
            if pathP[indexP] != pathQ[indexQ]:
                return pathP[indexP].parent
            indexP -= 1
            indexQ -= 1
        if indexP < 0:
            return pathP[0]
        if indexQ < 0:
            return pathQ[0]

import unittest

class TestSolution(unittest.TestCase):
    def testMinAddToMakeValid(self):
        s = Solution()
        self.assertEqual(s.minAddToMakeValid("())"), 1)
        self.assertEqual(s.minAddToMakeValid("((("), 3)


if __name__ == '__main__':
    unittest.main()