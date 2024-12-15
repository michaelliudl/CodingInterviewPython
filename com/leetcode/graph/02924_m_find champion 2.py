from typing import List

class Solution:

    # Find node with 0 in-degree
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        inDegrees = [0] * n
        for _, v in edges:
            inDegrees[v] += 1
        res = -1
        for i, inDegree in enumerate(inDegrees):
            if inDegree == 0:
                if res > -1:
                    return -1
                res = i
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testJump(self):
        s = Solution()
        self.assertEqual(s.jump(nums = [2,3,1,1,4]), 2)
        self.assertEqual(s.jump(nums = [2,3,0,1,4]), 2)
        self.assertEqual(s.jump(nums = [5,9,3,2,1,0,2,3,3,1,0,0]), 3)
        


if __name__ == '__main__':
    unittest.main()