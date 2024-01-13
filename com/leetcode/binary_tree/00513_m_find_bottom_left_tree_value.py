from typing import Optional,List,Deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
        

class Solution:

    def findBottomLeftValueRecur(self, root: Optional[TreeNode]) -> int:

        def dfs(node: TreeNode, depth: int, maxDepth: int) -> (int,int):
            if not node.left and not node.right:
                if depth>maxDepth:
                    return (node.val, depth)
            leftV,leftMaxD,rightV,rightMaxD=0,0,0,0
            if node.left:
                (leftV,leftMaxD)=dfs(node.left, depth+1, maxDepth)
            if node.right:
                (rightV,rightMaxD)=dfs(node.right, depth+1, maxDepth)
            return (leftV,leftMaxD) if leftMaxD>=rightMaxD else (rightV,rightMaxD)
        
        if not root:
            return 0
        return dfs(root, depth=1, maxDepth=-float('inf'))[0]


    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=Deque()
        q.append(root)
        r=root
        while q:
            r=q[0]
            size=len(q)
            for _ in range(size):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return r.val
        

import unittest

class TestSolution(unittest.TestCase):
    def testFindBottomLeftValue(self):
        s = Solution()
        
        self.assertEqual(s.findBottomLeftValue(TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))), 24)
        self.assertEqual(s.findBottomLeftValue(TreeNode(1)), 0)

        # self.assertEqual(s.sumOfLeftLeavesStack(TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))), 24)
        # self.assertEqual(s.sumOfLeftLeavesStack(TreeNode(1)), 0)

if __name__ == '__main__':
    unittest.main()