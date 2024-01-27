from typing import List

class TimeMap:

    def __init__(self):
        pass

    def set(self, key: str, value: str, timestamp: int) -> None:
        pass

    def get(self, key: str, timestamp: int) -> str:
        pass


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

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