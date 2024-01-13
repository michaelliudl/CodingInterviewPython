from typing import Optional,List,Deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
        

class Solution:

    def binaryTreePathsStack(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        r,st,visited=[],[],[]
        st.append(root)
        visited.append(root)
        while st:
            top=st[-1]
            if not top.left and not top.right:
                r.append('->'.join([str(node.val) for node in st]))
            if top.left and not top.left in visited:
                st.append(top.left)
                visited.append(top.left)
            elif top.right and not top.right in visited:
                st.append(top.right)
                visited.append(top.right)
            else:
                st.pop()
        return r

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        def dfs(node, r, path):
            if not node.left and not node.right:
                path.append(node.val)
                r.append('->'.join([str(p) for p in path]))
                return
            path.append(node.val)
            if node.left:
                dfs(node.left, r, path)
                path.pop()
            if node.right:
                dfs(node.right, r, path)
                path.pop()

        if not root:
            return []
        r=[]
        dfs(root, r, [])
        return r
    
    def binaryTreePathsRecurString(self, root: Optional[TreeNode]) -> List[str]:

        def dfs(node, r, path):
            if not node.left and not node.right:
                r.append(path+str(node.val))
                return
            path=path+str(node.val)
            if node.left:
                dfs(node.left, r, path+'->')
            if node.right:
                dfs(node.right, r, path+'->')

        if not root:
            return []
        r=[]
        dfs(root, r, '')
        return r


import unittest

class TestSolution(unittest.TestCase):
    def testBinaryTreePaths(self):
        s = Solution()
        
        self.assertEqual(s.binaryTreePaths(TreeNode(1,TreeNode(2,None,TreeNode(5)),TreeNode(3))), ["1->2->5","1->3"])
        self.assertEqual(s.binaryTreePaths(TreeNode(1)), ["1"])

        self.assertEqual(s.binaryTreePathsRecurString(TreeNode(1,TreeNode(2,None,TreeNode(5)),TreeNode(3))), ["1->2->5","1->3"])
        self.assertEqual(s.binaryTreePathsRecurString(TreeNode(1)), ["1"])

        self.assertEqual(s.binaryTreePathsStack(TreeNode(1,TreeNode(2,None,TreeNode(5)),TreeNode(3))), ["1->2->5","1->3"])
        self.assertEqual(s.binaryTreePathsStack(TreeNode(1)), ["1"])


if __name__ == '__main__':
    unittest.main()