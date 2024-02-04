from typing import Optional
from typing import List
from typing import Deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Codec:

    # Memory limit hit due to too many dummy nodes
    # Level order, result is from virtual complete binary tree
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ''
        ans,queue=[],Deque()
        queue.append(root)
        while queue:
            curLen=len(queue)
            lastLevel=True
            for _ in range(curLen):
                node=queue.popleft()
                if node.val == -float('inf'):
                    ans.append('\0')
                else:
                    ans.append(str(node.val))
                    if node.left:
                        queue.append(node.left)
                        lastLevel=False
                    else:
                        queue.append(TreeNode(val=-float('inf')))
                    if node.right:
                        queue.append(node.right)
                        lastLevel=False
                    else:
                        queue.append(TreeNode(val=-float('inf')))
            if lastLevel: break
        return ','.join(ans)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        def dfs(index):
            if index>=n: return None
            if values[index] == '\0': return None
            node=TreeNode(val=values[index])
            node.left=dfs(2*index+1)
            node.right=dfs(2*index+2)
            return node

        if not data: return None
        values=data.split(',')
        n=len(values)
        root=dfs(index=0)
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
        self.assertEqual(serialized, '1,2,3,\x00,\x00,4,5')
        newRoot=c.deserialize(serialized)
        # self.assertEqual(root,newRoot)

    def testCodec1(self):
        c=Codec()
        root=None
        serialized=c.serialize(root)
        self.assertEqual(serialized, '')
        newRoot=c.deserialize('')
        self.assertEqual(newRoot,None)

    def testCodec2(self):
        c=Codec()
        root=TreeNode(1,TreeNode(-2),TreeNode(3,TreeNode(4,TreeNode(6),TreeNode(7)),TreeNode(5)))
        serialized=c.serialize(root)
        self.assertEqual(serialized, '1,-2,3,\x00,\x00,4,5,6,7,\x00,\x00')
        newRoot=c.deserialize(serialized)
        self.assertEqual(root,newRoot)


if __name__ == '__main__':
    unittest.main()