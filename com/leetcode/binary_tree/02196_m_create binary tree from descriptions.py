from typing import Optional,List,Deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    # Map for value -> node. Set for children nodes.
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodeMap = {}
        childrenNodes = set()
        for pVal, cVal, isLeft in descriptions:
            pNode = nodeMap[pVal] if pVal in nodeMap else TreeNode(pVal)
            cNode = nodeMap[cVal] if cVal in nodeMap else TreeNode(cVal)
            if isLeft:
                pNode.left = cNode
            else:
                pNode.right = cNode
            nodeMap[pVal] = pNode
            nodeMap[cVal] = cNode
            childrenNodes.add(cNode)
        for node in nodeMap.values():
            if node not in childrenNodes:
                return node

import unittest

class TestSolution(unittest.TestCase):
    def testConstructMaximumBinaryTree(self):
        s = Solution()
        self.assertEqual(s.constructMaximumBinaryTree(nums = [3,2,1,6,0,5]), 
                         TreeNode(6,TreeNode(3,None,TreeNode(2,None(TreeNode(1)))), TreeNode(5,TreeNode(0))))


if __name__ == '__main__':
    unittest.main()