from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        pass

        

import unittest

class TestSolution(unittest.TestCase):
    def testRestoreIpAddresses(self):
        s = Solution()
        self.assertEqual(s.restoreIpAddresses(s = "25525511135"), ["255.255.11.135","255.255.111.35"])
        self.assertEqual(s.restoreIpAddresses(s = "0000"), ["0.0.0.0"])
        self.assertEqual(s.restoreIpAddresses(s = "101023"), ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"])


if __name__ == '__main__':
    unittest.main()