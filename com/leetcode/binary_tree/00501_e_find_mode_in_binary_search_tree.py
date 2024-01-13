from typing import Optional,List,Deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
        

class Solution:

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        prev,cur=None,root
        r,st=[],[]
        maxCount=0
        curCount=0
        while cur or st:
            if cur:
                st.append(cur)
                cur=cur.left
            else:
                cur=st.pop()
                if not prev:
                    curCount=1
                elif prev.val==cur.val:
                    curCount+=1
                else:
                    curCount=1
                if curCount==maxCount:
                    r.append(cur.val)
                if curCount>maxCount:
                    maxCount=curCount
                    r=[cur.val]
                prev=cur
                cur=cur.right
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