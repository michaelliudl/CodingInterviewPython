from typing import Optional,List,Deque

class Solution:

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xorPrefix = [0] * (len(arr) + 1)
        for index, elem in enumerate(arr):
            xorPrefix[index + 1] = xorPrefix[index] ^ elem
        res = [0] * len(queries)
        for index, [start, end] in enumerate(queries):
            res[index] = xorPrefix[start] ^ xorPrefix[end + 1]
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testSortByBits(self):
        s = Solution()
        self.assertEqual(s.sortByBits(arr = [0,1,2,3,4,5,6,7,8]), [0,1,2,4,8,3,5,6,7])
        self.assertEqual(s.sortByBits(arr = [1024,512,256,128,64,32,16,8,4,2,1]), [1,2,4,8,16,32,64,128,256,512,1024])

if __name__ == '__main__':
    unittest.main()