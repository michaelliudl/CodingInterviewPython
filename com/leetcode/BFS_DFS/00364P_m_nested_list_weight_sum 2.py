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
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        if not nestedList:
            return 0
        queue = Deque()
        for nested in nestedList:
            queue.append(nested)
        result = 0
        depthSum = 0
        while queue:
            curLen = len(queue)
            for _ in range(curLen):
                nested = queue.popleft()
                if nested.isInteger():
                    depthSum += nested.getInteger()     # Sum integers on each depth
                else:
                    for nestedInt in nested.getList():
                        queue.append(nestedInt)
            result += depthSum          # Lower depth elements are added again at deeper levels
        return result


    # DFS
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:

        def getDepth(myNestedList, depth):
            nonlocal maxDepth
            maxDepth = max(maxDepth, depth)
            for nestedInt in myNestedList:
                if nestedInt.getList():
                    getDepth(nestedInt.getList(), depth + 1)
        
        def getSum(myNestedList, depth):
            nonlocal result
            weight = maxDepth - depth + 1
            for nestedInt in myNestedList:
                if nestedInt.isInteger() and not nestedInt.getList():
                    result += weight * nestedInt.getInteger()
                else:
                    getSum(nestedInt.getList(), depth + 1)

        if not nestedList:
            return 0
        maxDepth = 0
        getDepth(nestedList, depth = 1)
        print(maxDepth)
        result = 0
        getSum(nestedList, depth = 1)
        return result

import unittest

class TestSolution(unittest.TestCase):
    def testHasCycle(self):
        s = Solution()
        self.assertEqual(s.hasCycle(ListNode(1,ListNode(2,None))), False)


if __name__ == '__main__':
    unittest.main()