from typing import List,Optional

class TreeNode:

    def __init__(self, val=0, left=None, right=None) -> None:
        self.val=val
        self.left=left
        self.right=right

class Solution:

    # Postorder traverse to update node values to one of below states
    # 0 not covered
    # 1 camera
    # 2 covered
    # Null nodes should be covered 2
    # Determine state of parent by checking its left and right
    # 
    # parent    left    right
    # 0         2       2       parent not covered if both children covered by lower level
    # 1         0       0(1,2)  camera if at one child is not covered
    # 1         0(1,2)  0
    # 2         1       1(2)    parent covered one child is camera and the other is camera or covered
    # 2         1(2)    1
    #
    # Check if root not covered, add last camera
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def postorder(node):
            nonlocal r
            if not node: return 2
            leftState=postorder(node.left)
            rightState=postorder(node.right)
            value=-1
            if leftState==2 and rightState==2:
                value=0
            elif leftState==0 or rightState==0:
                r+=1
                value=1
            elif (leftState==1 and rightState!=0) or (leftState!=0 and rightState==1):
                value=2
            node.val=value
            return value
        
        if not root: return 0
        r=0
        postorder(root)
        if root.val==0:
            root.val=1
            r+=1
        return r


import unittest

class TestSolution(unittest.TestCase):
    def testMinCameraCover(self):
        s = Solution()
        self.assertEqual(s.minCameraCover(TreeNode(0,TreeNode(0,TreeNode(0),TreeNode(0)))), 1)
        self.assertEqual(s.minCameraCover(TreeNode(0,TreeNode(0,TreeNode(0,TreeNode(0,None,TreeNode(0)))))), 2)
        


if __name__ == '__main__':
    unittest.main()