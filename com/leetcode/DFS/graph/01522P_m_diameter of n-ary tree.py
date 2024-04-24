from typing import List,Deque

'''
Given a root of an N-ary tree, you need to compute the length of the diameter of the tree.

The diameter of an N-ary tree is the length of the longest path between any two nodes in the tree. This path may or may not pass through the root.

(Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value.)
'''

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:

    # DFS each node and track max depth and second max depth among it's children
    # Diameter through current node is sum of max depth and second max depth
    # Return max depth + 1 to parent's consideration
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """

        def dfs(node):
            nonlocal result
            maxDep = secMaxDep = 0
            for child in node.children:
                dep = dfs(child)
                if dep > maxDep:
                    secMaxDep = maxDep
                    maxDep = dep
                elif dep > secMaxDep:
                    secMaxDep = dep
            result = max(result, maxDep + secMaxDep)
            return maxDep + 1
        
        if not root:
            return 0
        result = 0
        dfs(node = root)
        return result

import unittest

class TestSolution(unittest.TestCase):
    def testNumIslands(self):
        s = Solution()
        self.assertEqual(s.hasPath(maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]), False)
        self.assertEqual(s.hasPath(maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]), True)
        self.assertEqual(s.hasPath(maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], start = [4,3], destination = [0,1]), False)


if __name__ == '__main__':
    unittest.main()