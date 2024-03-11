from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        if len(s)==0:
            return True
        st=list()
        for c in s:
            if len(st)==0 and (c==')' or c==']' or c=='}'):
                return False
            st.append(c)
            if len(st)>1 and ((st[-2:]==['(',')']) or (st[-2:]==['[',']']) or (st[-2:]==['{','}'])):
                st.pop()
                st.pop()
        return len(st)==0

import unittest

class TestSolution(unittest.TestCase):
    def testIsValid(self):
        s = Solution()
        self.assertEqual(s.isValid("()"), True)
        self.assertEqual(s.isValid("()[]{}"), True)
        self.assertEqual(s.isValid("(]"), False)



if __name__ == '__main__':
    unittest.main()