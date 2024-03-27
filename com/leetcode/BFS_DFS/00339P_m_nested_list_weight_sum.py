from typing import List,Optional, Deque

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:

    # BFS
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        if not nestedList:
            return 0
        queue = Deque()
        for nested in nestedList:
            queue.append(nested)
        result = 0
        depth = 1
        while queue:
            curLen = len(queue)
            for _ in range(curLen):
                nested = queue.popleft()
                if nested.isInteger():
                    result += nested.getInteger() * depth
                else:
                    for nestedInt in nested.getList():
                        queue.append(nestedInt)
            depth += 1
        return result


    # DFS
    def depthSum(self, nestedList: List[NestedInteger]) -> int:

        def dfs(nestedList, depth):
            nonlocal result
            for nestedInt in nestedList:
                if nestedInt.isInteger():
                    result += nestedInt.getInteger() * depth
                else:
                    dfs(nestedInt.getList(), depth + 1)

        if not nestedList:
            return 0
        result = 0
        dfs(nestedList, depth = 1)
        return result

import unittest

class TestSolution(unittest.TestCase):
    def testHasCycle(self):
        s = Solution()
        self.assertEqual(s.hasCycle(ListNode(1,ListNode(2,None))), False)


if __name__ == '__main__':
    unittest.main()