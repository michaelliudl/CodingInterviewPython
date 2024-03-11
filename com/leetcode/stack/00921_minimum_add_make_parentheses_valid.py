from typing import List

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if not s or len(s)==0:
            return 0
        st=list()
        for c in s:
            if not (c=='(' or c==')'):
                return -1
            st.append(c)
            if len(st)>1 and st[len(st)-2:]==['(',')']:
                st.pop()
                st.pop()
        return len(st)

import unittest

class TestSolution(unittest.TestCase):
    def testMinAddToMakeValid(self):
        s = Solution()
        self.assertEqual(s.minAddToMakeValid("())"), 1)
        self.assertEqual(s.minAddToMakeValid("((("), 3)


if __name__ == '__main__':
    unittest.main()