from typing import Optional,List,Deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.arr.append(node)
            inorder(node.right)

        self.arr = [TreeNode(val=-float('inf'))]
        self.pointer = 0
        inorder(root)

    def next(self) -> int:
        if self.hasNext():
            self.pointer += 1
            return self.arr[self.pointer].val
        return -float('inf')

    def hasNext(self) -> bool:
        return self.pointer < len(self.arr) - 1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


class Solution:
    pass
    


import unittest

class TestSolution(unittest.TestCase):
    def testPathSum(self):
        s = Solution()
        self.assertEqual(s.pathSumStack(TreeNode(1,TreeNode(2)), 0), [])
        # self.assertEqual(s.pathSum(TreeNode(3,TreeNode(9,TreeNode(15),TreeNode(7)),TreeNode(20))), [3.00000,14.50000,11.00000])
        self.assertEqual(s.pathSumStack(None), [])


if __name__ == '__main__':
    unittest.main()