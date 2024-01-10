from typing import List

class Solution:
    def strStrBrute(self, haystack: str, needle: str) -> int:
        if not haystack or not needle or len(haystack)<len(needle):
            return -1
        for i in range(len(haystack)-len(needle)+1):
            m=True
            for j in range(len(needle)):
                if not needle[j]==haystack[i+j]:
                    m=False
                    break
            if m:
                return i
        return -1
    
    def strStrKMP(self, haystack: str, needle: str) -> int:
        if not haystack or not needle or len(haystack)<len(needle):
            return -1
        lps=self.getLps(needle)
        j=0
        for i in range(len(haystack)):
            while j>0 and haystack[i]!=needle[j]:
                j=lps[j-1]
            if haystack[i]==needle[j]:
                j+=1
            if j==len(needle):
                return i-j+1
        return -1


    def getLps(self, pattern: str) -> List:
        lps=[0]*len(pattern)
        j=0
        for i in range(1,len(pattern)):
            while j>0 and pattern[i]!=pattern[j]:
                j=lps[j-1]
            if pattern[i]==pattern[j]:
                j+=1
            lps[i]=j
        return lps

import unittest

class TestSolution(unittest.TestCase):
    def testStrStrBrute(self):
        s = Solution()
        # self.assertEqual(s.strStrBrute("sadbutsad","sad"), 0)
        # self.assertEqual(s.strStrBrute("leetcode","leeto"), -1)
        # self.assertEqual(s.strStrBrute("a","a"), 0)
        # self.assertEqual(s.strStrBrute("aaa","aa"), 0)
        # self.assertEqual(s.strStrBrute("mississippi","issipi"), -1)

    def testStrStrKMP(self):
        s = Solution()
        # self.assertEqual(s.strStrKMP("sadbutsad","sad"), 0)
        # self.assertEqual(s.strStrKMP("leetcode","leeto"), -1)
        # self.assertEqual(s.strStrKMP("a","a"), 0)
        # self.assertEqual(s.strStrKMP("aaa","aa"), 0)
        # self.assertEqual(s.strStrKMP("mississippi","issipi"), -1)
        self.assertEqual(s.strStrKMP("hello","ll"), 2)


if __name__ == '__main__':
    unittest.main()