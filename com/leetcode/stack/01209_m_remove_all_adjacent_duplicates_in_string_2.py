from typing import List

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if not s or k<=0: return s
        st=[]
        for c in s:
            if st and c==st[-1][0]:
                st.append((c, st[-1][1]+1))     # Push with consecutive count
            else:
                st.append((c, 1))
            if st[-1][1]==k:
                for _ in range(k):
                    st.pop()
        return ''.join([pair[0] for pair in st])

import unittest

class TestSolution(unittest.TestCase):
    def testRemoveDuplicates(self):
        s = Solution()
        self.assertEqual(s.removeDuplicates(s = "abcd", k = 2), "abcd")
        self.assertEqual(s.removeDuplicates(s = "deeedbbcccbdaa", k = 3), "aa")
        self.assertEqual(s.removeDuplicates(s = "pbbcggttciiippooaais", k = 2), "ps")



if __name__ == '__main__':
    unittest.main()