from typing import List
import heapq

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