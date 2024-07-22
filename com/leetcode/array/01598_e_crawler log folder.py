from typing import List

class Solution:

    def minOperations(self, logs: List[str]) -> int:
        res = 0
        for log in logs:
            if log == '../':
                res -= (1 if res > 0 else 0)
            elif log != './':
                res += 1
        return res

        

import unittest

class TestSolution(unittest.TestCase):

    def testPivotIndex(self):
        s=Solution()
        self.assertEqual(s.pivotIndex(nums = [1,7,3,6,5,6]), 3)
        self.assertEqual(s.pivotIndex(nums = [2,1,-1]), 0)
        self.assertEqual(s.pivotIndex(nums = [1,2,3]), -1)

if __name__ == '__main__':
    unittest.main()