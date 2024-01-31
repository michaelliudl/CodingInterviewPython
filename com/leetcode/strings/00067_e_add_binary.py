from typing import List

class Solution:

    def addBinary(self, a: str, b: str) -> str:
        if not a and not b: return ''
        if not a: return b
        if not b: return a

        r=[]
        carry,m,n=0,len(a),len(b)
        i,j=m-1,n-1
        while i>=0 and j>=0:
            numa,numb=int(a[i]),int(b[j])
            s=numa+numb+carry
            r.append(str(s%2))
            carry=s//2
            i-=1
            j-=1
        while i>=0:
            s=int(a[i])+carry
            r.append(str(s%2))
            carry=s//2
            i-=1
        while j>=0:
            s=int(b[j])+carry
            r.append(str(s%2))
            carry=s//2
            j-=1
        if carry>0: r.append(str(carry))
        low,high=0,len(r)-1
        while low<high:
            r[low],r[high]=r[high],r[low]
            low+=1
            high-=1
        return ''.join(r)
                       


import unittest

class TestSolution(unittest.TestCase):
    def testIsLongPressedName(self):
        s = Solution()
        self.assertEqual(s.isLongPressedName(name = "alex", typed = "aaleexx"), True)
        self.assertEqual(s.isLongPressedName(name = "alex", typed = "aaleexxxxx"), True)
        self.assertEqual(s.isLongPressedName(name = "saeed", typed = "ssaaedd"), False)
        self.assertEqual(s.isLongPressedName(name = "leelee", typed = "lleeelee"), True)
        self.assertEqual(s.isLongPressedName(name = "alex", typed = "aaleexabc"), False)
        self.assertEqual(s.isLongPressedName(name = "alexabc", typed = "aaleexxxxxx"), False)


if __name__ == '__main__':
    unittest.main()