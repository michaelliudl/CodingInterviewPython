from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        def lca():
            n=min(len(startPath),len(destPath))
            for i in range(n):
                startNode,_=startPath[i]
                destNode,_=destPath[i]
                if startNode==destNode:
                    if i==n-1:
                        return i
                    startNextNode,_=startPath[i+1]
                    destNextNode,_=destPath[i+1]
                    if startNextNode!=destNextNode:
                        return i
        
        def dfs(node,value,path):
            nonlocal found,curPath
            if found: return
            if node.val==value:
                path.append((node,''))
                curPath=path[:]
                found=True
                path.pop()
                return
            if node.left:
                path.append((node, 'L'))
                dfs(node.left,value,path)
                path.pop()
            if node.right:
                path.append((node, 'R'))
                dfs(node.right,value,path)
                path.pop()

        if not root: return ''
        curPath=[]
        found=False
        dfs(root,value=startValue,path=[])
        startPath=curPath[:]
        found=False
        dfs(root,value=destValue,path=[])
        destPath=curPath[:]

        lcaIndex=lca()
            
        path=[]
        for _ in range(len(startPath)-2,lcaIndex-1,-1):
            path.append('U')
        for i in range(lcaIndex,len(destPath)-1):
            path.append(destPath[i][1])
        return ''.join(path)

import unittest

class TestSolution(unittest.TestCase):
    def testGetDirections(self):
        s = Solution()
        self.assertEqual(s.getDirections(root=TreeNode(5,None,TreeNode(3,TreeNode(4),TreeNode(7))), startValue = 4, destValue = 3), 'U')
        self.assertEqual(s.getDirections(root=TreeNode(5,TreeNode(1,TreeNode(3)),TreeNode(2,TreeNode(6),TreeNode(4))), startValue = 3, destValue = 6), 'UURL')
        self.assertEqual(s.getDirections(root=TreeNode(2,TreeNode(1)), startValue = 2, destValue = 1), 'L')
        self.assertEqual(s.getDirections(root=TreeNode(1,None,TreeNode(10,TreeNode(12,TreeNode(4),TreeNode(6)),TreeNode(13,None,TreeNode(15,None,TreeNode(2))))),
                                         startValue = 6, destValue = 15), 'UURR')


if __name__ == '__main__':
    unittest.main()