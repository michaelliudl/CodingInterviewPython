from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not root or not p or not q:
            return None
        pl,ql=list(),list()
        self.findPath(root,p,pl),self.findPath(root,q,ql)
        

import unittest

class TestSolution(unittest.TestCase):
    def testMinAddToMakeValid(self):
        s = Solution()
        self.assertEqual(s.minAddToMakeValid("())"), 1)
        self.assertEqual(s.minAddToMakeValid("((("), 3)


if __name__ == '__main__':
    unittest.main()