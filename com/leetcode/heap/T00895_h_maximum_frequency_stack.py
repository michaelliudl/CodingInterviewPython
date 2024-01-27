from typing import List
import heapq

class FreqStack:

    def __init__(self):
        pass

    def push(self, val: int) -> None:
        pass

    def pop(self) -> int:
        pass


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pass


import unittest

class TestSolution(unittest.TestCase):
    def testTopKFrequent(self):
        s = Solution()
        self.assertEqual(set(s.topKFrequent([1,1,1,2,2,3],k=2)), set([1,2]))
        self.assertEqual(s.topKFrequent([1],k=1), [1])



if __name__ == '__main__':
    unittest.main()