from typing import List

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pass

import unittest

class TestSolution(unittest.TestCase):
    def testFindErrorNums(self):
        s = Solution()
        self.assertEqual(s.findErrorNums(nums = [1,2,2,4]), [2,3])
        self.assertEqual(s.findErrorNums(nums = [1,1]), [1,2])
        self.assertEqual(s.findErrorNums(nums = [2,2]), [2,1])
        


if __name__ == '__main__':
    unittest.main()