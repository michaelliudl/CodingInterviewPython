from typing import Optional,List,Deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
        

class Solution:

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def recur(low, high):
            if low>high: return None
            for i in range(low,high+1):



        if n<=0: return []
        vals=[i+1 for i in range(n)]
        r=[]
        for i in range(n):
            if i
        recur(low=0, high=n-1)

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