from typing import Optional,List,Deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def recur(pre: list, ino: list, startPre: int, endPre:int, startIn: int, endIn: int) -> TreeNode:
            if startPre>endPre or startIn>endIn:
                return None
            rootV=pre[startPre]
            rootI=startIn
            for i in range(startIn, endIn+1):
                if ino[i]==rootV:
                    rootI=i
            lenLeftSub=rootI-startIn
            return (TreeNode(rootV,
                            recur(pre, ino, startPre+1, startPre+lenLeftSub, startIn, rootI-1),
                            recur(pre, ino, startPre+lenLeftSub+1, endPre, rootI+1, endIn)))

        if not preorder or not inorder or len(preorder)!=len(inorder):
            return None
        return recur(preorder, inorder, 0, len(preorder)-1, 0, len(inorder)-1)
        

import unittest

class TestSolution(unittest.TestCase):
    def testBuildTree(self):
        s = Solution()
        self.assertEqual(s.buildTree([2,1],[2,1]), TreeNode(1,TreeNode(2)))


if __name__ == '__main__':
    unittest.main()