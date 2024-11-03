from typing import List

class Solution:

    def parseBoolExpr(self, expression: str) -> bool:
        pass

import unittest

class TestSolution(unittest.TestCase):

    def testSequentialDigits(self):
        s = Solution()
        self.assertEqual(s.sequentialDigits(low = 100, high = 300), [123,234])
        self.assertEqual(s.sequentialDigits(low = 1000, high = 13000), [1234,2345,3456,4567,5678,6789,12345])

if __name__ == '__main__':
    unittest.main()