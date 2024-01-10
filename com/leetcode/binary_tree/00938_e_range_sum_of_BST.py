from typing import List,Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root or low<0 or high<low:
            return -1
        sum=self.rangeSum(root, low, high)
        return sum
        

    def rangeSum(self, root, low, high) -> int:
        if not root:
            return 0
        sum=root.val if root.val>=low and root.val<=high else 0
        sum+=self.rangeSum(root.left, low, high)
        sum+=self.rangeSum(root.right, low, high)
        return sum


import unittest

class TestSolution(unittest.TestCase):
    def testRangeSumBST(self):
        s = Solution()
        self.assertEqual(s.rangeSumBST(
            TreeNode(10,TreeNode(5,TreeNode(3),TreeNode(7)),TreeNode(15,None,TreeNode(18))), low=7, high=15
        ), 32)
        self.assertEqual(s.rangeSumBST(
            TreeNode(10,TreeNode(5,TreeNode(3,TreeNode(1),None),TreeNode(7,TreeNode(6),None)),TreeNode(15,TreeNode(13),TreeNode(18))), low=6, high=10
        ), 23)


if __name__ == '__main__':
    unittest.main()