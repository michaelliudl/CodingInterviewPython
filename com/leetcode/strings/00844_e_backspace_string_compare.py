from typing import List

class Solution:

    # Without using stack
    def backspaceCompare(self, s: str, t: str) -> bool:
        if not s and not t: return True
        if not s or not t: return False
        i,j,sCount,tCount=len(s)-1,len(t)-1,0,0
        while True:
            while i>=0 and s[i]=='#':
                sCount+=1
                i-=1
            while sCount>0:
                if s[i]=='#':
                    break
                else:
                    sCount-=1
                    i-=1
            if i>=0 and s[i]=='#':
                continue
            
            while j>=0 and t[j]=='#':
                tCount+=1
                j-=1
            while tCount>0:
                if t[j]=='#':
                    break
                else:
                    tCount-=1
                    j-=1
            if j>=0 and t[j]=='#':
                continue

            if i<0 and j<0:
                return True
            elif (i<0 and j>=0) or (i>=0 and j<0):
                return False
            elif i>=0 and j>=0:
                if s[i]!=t[j]:
                    return False
                while s[i]==t[j] and s[i]!='#' and t[j]!='#':
                    i-=1
                    j-=1



import unittest

class TestSolution(unittest.TestCase):
    def testBackspaceCompare(self):
        s = Solution()
        # self.assertEqual(s.backspaceCompare(s = "ab#c", t = "ad#c"), True)
        # self.assertEqual(s.backspaceCompare(s = "ab##", t = "c#d#"), True)
        # self.assertEqual(s.backspaceCompare(s = "a#c", t = "b"), False)
        self.assertEqual(s.backspaceCompare(s = "bxj##tw", t = "bxo#j##tw"), True)


if __name__ == '__main__':
    unittest.main()