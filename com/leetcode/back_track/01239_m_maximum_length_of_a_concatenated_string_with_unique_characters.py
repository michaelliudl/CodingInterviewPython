from typing import List

class Solution:

    def maxLength(self, arr: List[str]) -> int:
        def backtrack(startIndex, r, ul):
            if ul>r:
                r=ul
            for i in range(startIndex,n):
                unique=True
                added={}
                for c in arr[i]:
                    if c in cache and cache[c]>0:
                        unique=False
                        break
                    cache[c]=1
                    added[c]=1
                if not unique:
                    for c in added:
                        cache[c]=0
                    continue
                ul+=len(arr[i])
                r=backtrack(i+1, r, ul)
                for c in arr[i]:
                    cache[c]=0
                    ul-=1
            return r
        

        if not arr:
            return 0
        r,n=0,len(arr)
        cache={}
        r=backtrack(startIndex=0, r=r, ul=0)
        return r


import unittest

class TestSolution(unittest.TestCase):
    def testMaxLength(self):
        s = Solution()
        self.assertEqual(s.maxLength(arr = ["un","iq","ue"]), 4)
        self.assertEqual(s.maxLength(arr = ["cha","r","act","ers"]), 6)
        self.assertEqual(s.maxLength(arr = ["abcdefghijklmnopqrstuvwxyz"]), 26)
        


if __name__ == '__main__':
    unittest.main()