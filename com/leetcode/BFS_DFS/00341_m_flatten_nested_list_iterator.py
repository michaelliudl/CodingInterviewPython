from typing import Optional,List,Deque

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:

    # Queue and recursively enqueue integers within nested lists
    def __init__(self, nestedList: [NestedInteger]):

        def enqueue(nestedList):
            for nested in nestedList:
                if nested.isInteger():
                    self.queue.append(nested.getInteger())
                else:
                    enqueue(nested.getList())

        self.queue = Deque()
        enqueue(nestedList)
    
    def next(self) -> int:
        if self.queue:
            return self.queue.popleft()
        return -1
    
    def hasNext(self) -> bool:
        return len(self.queue) > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

class Solution:
    pass

import unittest

class TestSolution(unittest.TestCase):
    def testNestedIterator(self):
        ni = NestedIterator()
        self.assertEqual(ni.hasNext(), True)


if __name__ == '__main__':
    unittest.main()