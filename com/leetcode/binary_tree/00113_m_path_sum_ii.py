from typing import Optional,List,Deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def dfs(node: TreeNode, rem: int, r: list, path: list):
            if not node.left and not node.right:
                path.append(node.val)
                if rem==node.val:
                    r.append(path[:])
                return
            path.append(node.val)
            if node.left:
                dfs(node.left, rem-node.val, r, path)
                path.pop()
            if node.right:
                dfs(node.right, rem-node.val, r, path)
                path.pop()

        if not root:
            return []
        r,path=[],[]
        dfs(root, targetSum, r, path)
        return r
    
    def pathSumStack(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        st,r=[(root, [root.val])],[]
        while st:
            (node,path)=st.pop()
            if not node.left and not node.right:
                if sum(path)==targetSum:
                    r.append(path)
            if node.left:
                st.append((node.left, path+[node.left.val]))
            if node.right:
                st.append((node.right, path+[node.right.val]))
        return r


import unittest

class TestSolution(unittest.TestCase):
    def testPathSum(self):
        s = Solution()
        self.assertEqual(s.pathSumStack(TreeNode(1,TreeNode(2)), 0), [])
        # self.assertEqual(s.pathSum(TreeNode(3,TreeNode(9,TreeNode(15),TreeNode(7)),TreeNode(20))), [3.00000,14.50000,11.00000])
        self.assertEqual(s.pathSumStack(None), [])


if __name__ == '__main__':
    unittest.main()