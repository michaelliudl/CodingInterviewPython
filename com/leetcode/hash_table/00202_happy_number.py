from typing import List

class Solution:
    def isHappy(self, n: int) -> bool:
        if n<=0:
            return False
        ss=dict()
        x=n
        ss[x]=1
        while True:
            l=list()
            while x>0:
                l.append(x%10)
                x=int(x/10)
            x=sum([y*y for y in l])
            if x==1:
                return True
            if x in ss:
                return False
            ss[x]=1
        return False

import unittest

class TestSolution(unittest.TestCase):
    def testIsHappy(self):
        s = Solution()
        self.assertEqual(s.isHappy(19), True)
        self.assertEqual(s.isHappy(2), False)


if __name__ == '__main__':
    unittest.main()