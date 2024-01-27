from typing import List

class MyCalendar:

    def __init__(self):
        pass

    def book(self, start: int, end: int) -> bool:
        pass


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

class Solution:
    pass


import unittest

class TestSolution(unittest.TestCase):
    def testFindRedundantConnection(self):
        s = Solution()
        self.assertEqual(s.findRedundantConnection(edges = [[1,2],[1,3],[2,3]]), [2,3])
        self.assertEqual(s.findRedundantConnection(edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]), [1,4])
        # self.assertEqual(s.findRedundantConnection([0,0,0]), [[0,0,0]])


if __name__ == '__main__':
    unittest.main()