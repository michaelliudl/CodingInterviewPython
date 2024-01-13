from typing import Optional,List,Deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def recur(inor: list, postor: list, startIn: int, endIn: int, startPost: int, endPost: int) -> TreeNode:
            if startIn>endIn or startPost>endPost:
                return None
            rootV=postor[endPost]
            rootI=0
            for i in range(startIn,endIn+1):
                if inor[i]==rootV:
                    rootI=i
            lenLeftSub=rootI-startIn
            root=TreeNode(rootV)
            root.left=recur(inor, postor, startIn, rootI-1, startPost, (startPost+(lenLeftSub-1)))
            root.right=recur(inor, postor, rootI+1, endIn, startPost+lenLeftSub, endPost-1)
            return root

        if not inorder or not postorder or len(inorder)!=len(postorder):
            return None
        n=len(inorder)
        return recur(inorder, postorder, 0, n-1, 0, n-1)
        

    def buildTreeArrayCopy(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder or len(inorder)!=len(postorder):
            return None
        rootV=postorder[-1]
        root=TreeNode(rootV)
        rootI=0
        for i,v in enumerate(inorder):
            if v==rootV:
                rootI=i
        root.left=self.buildTree(inorder[:rootI], postorder[:rootI])
        root.right=self.buildTree(inorder[rootI+1:], postorder[rootI:-1])
        return root

import unittest

class TestSolution(unittest.TestCase):
    def testBuildTree(self):
        s = Solution()
        self.assertEqual(s.buildTree([2,1],[2,1]), TreeNode(1,TreeNode(2)))


if __name__ == '__main__':
    unittest.main()