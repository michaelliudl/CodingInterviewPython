from typing import List

class MinStack:

    def __init__(self):
        pass

    def push(self, val: int) -> None:
        pass

    def pop(self) -> None:
        pass

    def top(self) -> int:
        pass

    def getMin(self) -> int:
        pass
    
class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            return None
        l=[s for s in path.split('/') if s]
        st=list()
        for s in l:
            if s=='.':
                continue
            if s=='..':
                if len(st)>0:
                    st.pop()
                continue
            st.append(s)
        return '/'+'/'.join(st)


import unittest

class TestSolution(unittest.TestCase):
    def testSimplifyPath(self):
        s = Solution()
        self.assertEqual(s.simplifyPath("/home/"), "/home")
        self.assertEqual(s.simplifyPath("/../"), "/")
        self.assertEqual(s.simplifyPath("/home//foo/"), "/home/foo")



if __name__ == '__main__':
    unittest.main()