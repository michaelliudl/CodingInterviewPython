from typing import List

class Solution:

    def monotoneIncreasingDigits(self, n: int) -> int:
        if n<10: return n
        s=str(n)
        flag=len(s)
        l=[]
        for i in range(len(s)):
            l.append(int(s[i]))
        for i in range(len(l)-1,0,-1):
            if l[i-1]>l[i]:
                flag=i
                l[i-1]-=1
        for i in range(flag,len(l)):
            l[i]=9
        r,m=0,1
        for i in range(len(l)-1,-1,-1):
            r+=l[i]*m
            m*=10
        return r
                


import unittest

class TestSolution(unittest.TestCase):
    def testMonotoneIncreasingDigits(self):
        s = Solution()
        self.assertEqual(s.monotoneIncreasingDigits(n=10), 9)
        self.assertEqual(s.monotoneIncreasingDigits(n=1234), 1234)
        self.assertEqual(s.monotoneIncreasingDigits(n=332), 299)
        self.assertEqual(s.monotoneIncreasingDigits(n=100), 99)
        self.assertEqual(s.monotoneIncreasingDigits(n=101), 99)
        


if __name__ == '__main__':
    unittest.main()