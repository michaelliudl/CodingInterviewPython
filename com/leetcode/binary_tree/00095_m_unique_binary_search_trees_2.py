from typing import Optional,List,Deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
        

class Solution:

    # Use top-down approach then combine
    # Use memoization
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def genTrees(low, high):
            if low > high:
                mem[(low, high)] = [None]
                return [None]
            if (low, high) in mem:
                return mem[(low, high)]
            trees = []
            for i in range(low, high + 1):
                leftTrees = genTrees(low, i - 1)
                rightTrees = genTrees(i + 1, high)
                for left in leftTrees:
                    for right in rightTrees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        trees.append(root)
            mem[(low, high)] = trees
            return trees

        if n <= 0:
            return []
        mem = {}
        result = genTrees(1, n)
        return result

import unittest

class TestSolution(unittest.TestCase):
    def testGenerateTrees(self):
        s = Solution()
        s.generateTrees(3)
        
if __name__ == '__main__':
    unittest.main()