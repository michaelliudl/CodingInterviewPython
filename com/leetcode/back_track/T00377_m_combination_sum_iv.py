from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        

import unittest

class TestSolution(unittest.TestCase):
    def testCombine(self):
        s = Solution()
        self.assertEqual(s.combine(4,2), [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]])
        self.assertEqual(s.combine(1,1), [[1]])
        self.assertEqual(s.combine(5,3), [[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5],[3,4,5]])


if __name__ == '__main__':
    unittest.main()