from typing import List

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if not s or k<=0: return 0
        vowels=('a','e','i','o','u')
        lim=min(k,len(s))
        subTotal=0
        for i in range(lim):
            if s[i] in vowels:
                subTotal+=1
        ans=subTotal
        for i in range(k,len(s)):
            winIn,winOut=s[i],s[i-k]
            if winIn in vowels: subTotal+=1
            if winOut in vowels: subTotal-=1
            ans = max(ans, subTotal)
        return ans


import unittest

class TestSolution(unittest.TestCase):
    def testminWindow(self):
        s = Solution()
        self.assertEqual(s.minWindow(s = "ADOBECODEBANC", t = "ABC"), "BANC")
        self.assertEqual(s.minWindow(s = "a", t = "a"), 'a')
        self.assertEqual(s.minWindow(s = "a", t = "aa"), '')


if __name__ == '__main__':
    unittest.main()