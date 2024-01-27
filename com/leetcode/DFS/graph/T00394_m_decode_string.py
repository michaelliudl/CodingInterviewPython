from typing import Optional,List,Deque



class Solution:

    def decodeString(self, s: str) -> str:
        pass

import unittest

class TestSolution(unittest.TestCase):
    def testConstructMaximumBinaryTree(self):
        s = Solution()
        self.assertEqual(s.constructMaximumBinaryTree(nums = [3,2,1,6,0,5]), 
                         TreeNode(6,TreeNode(3,None,TreeNode(2,None(TreeNode(1)))), TreeNode(5,TreeNode(0))))


if __name__ == '__main__':
    unittest.main()