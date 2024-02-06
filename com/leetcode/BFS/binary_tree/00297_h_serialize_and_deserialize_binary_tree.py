from typing import Optional
from typing import List
from typing import Deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

# DFS
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preorder(node):
            if not node:
                ans.append('\x00')
                return
            ans.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        if not root: return ''
        ans = []
        preorder(root)
        return ','.join(ans)
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def preorder():
            value = queue.popleft()
            if value == '\x00':
                return None
            node = TreeNode(int(value))
            node.left = preorder()
            node.right = preorder()
            return node

        if not data: return None
        values=data.split(',')
        n=len(values)
        queue = Deque()
        for value in values: queue.append(value)
        return preorder()

# BFS
class CodecBFS:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ''
        ans,queue=[],Deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node:
                ans.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                ans.append('\x00')
        end = len(ans) - 1
        for i in range(len(ans)-1, -1, -1):
            if ans[i] != '\x00':
                end = i
                break
        return ','.join(ans[:(end+1)])
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        values=data.split(',')
        n=len(values)
        queue = Deque()
        root = TreeNode(int(values[0]))
        queue.append(root)
        for i in range(1, len(values), 2):
            node = queue.popleft()
            leftValue, rightValue = values[i], values[i+1] if i+1 < len(values) else '\x00'
            left = TreeNode(int(leftValue)) if leftValue != '\x00' else None
            right = TreeNode(int(rightValue)) if rightValue != '\x00' else None
            node.left = left
            node.right = right
            if left:
                queue.append(left)
            if right:
                queue.append(right)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

class Solution:
    pass
    

import unittest

class TestSolution(unittest.TestCase):
    def testCodec(self):
        c=Codec()
        root=TreeNode(1,TreeNode(2),TreeNode(3,TreeNode(4),TreeNode(5)))
        serialized=c.serialize(root)
        # self.assertEqual(serialized, '1,2,3,\x00,\x00,4,5')               # BFS
        self.assertEqual(serialized, '1,2,\x00,\x00,3,4,\x00,\x00,5,\x00,\x00')               # DFS
        newRoot=c.deserialize(serialized)
        self.assertEqual(root.val, newRoot.val)

    def testCodec1(self):
        c=Codec()
        root=None
        serialized=c.serialize(root)
        self.assertEqual(serialized, '')
        newRoot=c.deserialize('')
        self.assertEqual(newRoot, None)

    def testCodec2(self):
        c=Codec()
        root=TreeNode(1,TreeNode(-2),TreeNode(3,TreeNode(4,TreeNode(6),TreeNode(7)),TreeNode(5)))
        serialized=c.serialize(root)
        # self.assertEqual(serialized, '1,-2,3,\x00,\x00,4,5,6,7')          # BFS
        self.assertEqual(serialized, '1,-2,\x00,\x00,3,4,6,\x00,\x00,7,\x00,\x00,5,\x00,\x00')          # DFS
        newRoot=c.deserialize(serialized)
        self.assertEqual(root.val, newRoot.val)


if __name__ == '__main__':
    unittest.main()