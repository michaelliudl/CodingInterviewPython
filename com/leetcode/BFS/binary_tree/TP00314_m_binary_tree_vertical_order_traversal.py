from typing import Optional
from typing import List
from typing import Deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    # Vertical order. Difference with 987?
    def levelOrderIter(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        r=[]
        q=Deque()
        q.append(root)
        while q:
            qLen=len(q)
            r1=[]
            for _ in range(qLen):
                node=q.popleft()
                r1.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            r.append(r1)
        return r

    def levelOrderIterTwoQueues(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        r=[]
        q,q1=Deque(),Deque()
        q.append(root)
        while q:
            while q:
                q1.append(q.popleft())
            r1=[]
            while q1:
                tn=q1.popleft()
                r1.append(tn.val)
                if tn.left:
                    q.append(tn.left)
                if tn.right:
                    q.append(tn.right)
            r.append(r1)
        return r
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        r=[]
        self.levelTraverse(root,0,r)
        return r

    def levelTraverse(self, node: TreeNode, level: int, r: list):
        if not node:
            return
        if len(r)==level:
            r.append([])
        r[level].append(node.val)
        self.levelTraverse(node.left, level+1,r)
        self.levelTraverse(node.right,level+1,r)
    

import unittest

class TestSolution(unittest.TestCase):
    def testLevelOrder(self):
        s = Solution()
        self.assertEqual(s.levelOrderIter(TreeNode(3,TreeNode(9,None,None),TreeNode(20,TreeNode(15,None,None),TreeNode(7,None,None)))), [[3],[9,20],[15,7]])
        self.assertEqual(s.levelOrderIter(None), [])
        self.assertEqual(s.levelOrderIter(TreeNode(1,None,None)), [[1]])


if __name__ == '__main__':
    unittest.main()