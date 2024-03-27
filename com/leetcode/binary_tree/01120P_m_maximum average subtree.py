from typing import Optional,List,Deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
        

class Solution:

    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:

        def maxAvgSub(node):
            nonlocal result
            if not node:
                return (0, 0)
            leftSum, leftCount = maxAvgSub(node.left)
            rightSum, rightCount = maxAvgSub(node.right)
            curSum = leftSum + node.val + rightSum
            curCount = leftCount + 1 + rightCount
            leftAvg = leftSum / leftCount if leftCount > 0 else 0
            rightAvg = rightSum / rightCount if rightCount > 0 else 0
            curAvg = curSum / curCount if curCount > 0 else 0
            result = max(result, leftAvg, curAvg, rightAvg)
            return (curSum, curCount)

        if not root:
            return 0
        result = -float('inf')
        maxAvgSub(root)
        return result

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