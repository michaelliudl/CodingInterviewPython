from typing import List

class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return None
        l=[w for w in s.split(" ") if w]
        i,j=0,len(l)-1
        while i<j:
            l[i],l[j]=l[j],l[i]
            i+=1
            j-=1
        return " ".join(l)
    
    def reverseWordsChars(self, s: str) -> str:
        if not s:
            return None
        cl1=[c for c in s]
        cl=[]
        i=0
        while i<len(cl1):
            cl.append(cl1[i])
            if cl1[i]!=' ' or (cl1[i]==' ' and i+1<len(cl1) and cl1[i+1]!=' '):
                i+=1
                continue
            if cl1[i]==' ' and i+1<len(cl1) and cl1[i+1]==' ':
                while i<len(cl1) and cl1[i]==' ':
                    i+=1
        if cl[0]==' ':
            cl=cl[1:]
        if cl[len(cl)-1]==' ':
            cl=cl[:len(cl)-1]
        l,r=0,len(cl)-1
        while l<r:
            cl[l],cl[r]=cl[r],cl[l]
            l+=1
            r-=1
        l,r=0,0
        for i in range(len(cl)):
            if cl[i]!=' ':
                continue
            r=i-1
            s,e=l,r
            while s<e:
                cl[s],cl[e]=cl[e],cl[s]
                s+=1
                e-=1
            l=i+1
        r=len(cl)-1
        while l<r:
            cl[l],cl[r]=cl[r],cl[l]
            l+=1
            r-=1
        return "".join(cl)



import unittest

class TestSolution(unittest.TestCase):
    def testReverseWords(self):
        s = Solution()
        self.assertEqual(s.reverseWordsChars(s = "the sky is blue"), "blue is sky the")
        self.assertEqual(s.reverseWordsChars(s = "  hello world  "), "world hello")
        self.assertEqual(s.reverseWordsChars(s = "a good   example"), "example good a")


if __name__ == '__main__':
    unittest.main()