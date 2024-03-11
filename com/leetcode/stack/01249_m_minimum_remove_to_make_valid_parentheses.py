from typing import List

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s:
            return s
        st=[]
        for i in range(len(s)):
            if s[i] in ('(',')'):
                st.append((s[i],i))
                if len(st)>1 and st[-1][0]==')' and st[-2][0]=='(':
                    st.pop()
                    st.pop()
        if not st:
            return s
        r=[]
        last=0
        for t in st:
            cur=t[1]
            r.append(s[last:cur])
            last=cur+1
        r.append(s[last:])
        return ''.join(r)




import unittest

class TestSolution(unittest.TestCase):
    def testMinRemoveToMakeValid(self):
        s = Solution()
        self.assertEqual(s.minRemoveToMakeValid(s = "lee(t(c)o)de)"), "lee(t(c)o)de")
        self.assertEqual(s.minRemoveToMakeValid(s = "a)b(c)d"), "ab(c)d")
        self.assertEqual(s.minRemoveToMakeValid(s = "))(("), "")



if __name__ == '__main__':
    unittest.main()