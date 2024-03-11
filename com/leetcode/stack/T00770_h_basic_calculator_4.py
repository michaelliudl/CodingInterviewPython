from typing import List

class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        pass

import unittest

class TestSolution(unittest.TestCase):
    def testCalculate(self):
        s = Solution()
        self.assertEqual(s.calculate(s = "1 + 1"), 2)
        self.assertEqual(s.calculate(s = " 2-1 + 2 "), 3)
        self.assertEqual(s.calculate(s = "(1+(4+5+2)-3)+(6+8)"), 23)



if __name__ == '__main__':
    unittest.main()