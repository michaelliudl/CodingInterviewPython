from typing import List

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if not s or k<0:
            return None
        n=len(s)
        sl=[c for c in s]
        for i in range(0,n,2*k):
            l=i
            r=i+k-1
            if r>=n:
                r=n-1
            while l<r:
                sl[l],sl[r]=sl[r],sl[l]
                l+=1
                r-=1
        return "".join(sl)

import unittest

class TestSolution(unittest.TestCase):
    def testReverseStr(self):
        s = Solution()
        self.assertEqual(s.reverseStr("abcdefg",2), "bacdfeg")
        self.assertEqual(s.reverseStr("abcd",2), "bacd")


if __name__ == '__main__':
    unittest.main()