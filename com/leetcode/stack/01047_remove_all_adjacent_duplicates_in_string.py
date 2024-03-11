from typing import List

class Solution:
    def removeDuplicates(self, s: str) -> str:
        st=list()
        for c in s:
            if len(st)==0 or st[-1]!=c:
                st.append(c)
            elif st[-1]==c:
                st.pop()
        return ''.join(st)

import unittest

class TestSolution(unittest.TestCase):
    def testRemoveDuplicates(self):
        s = Solution()
        self.assertEqual(s.removeDuplicates("abbaca"), "ca")
        self.assertEqual(s.removeDuplicates("azxxzy"), "ay")


if __name__ == '__main__':
    unittest.main()