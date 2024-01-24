from typing import List
import heapq,math

class Solution:

    # Complete backpack that chooses any words from dict and forms s
    # dp[i] is True if dp[j] is True and s[j:i+1) is in dict (j<i)
    # Words order determines result, so it's permutation
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s or not wordDict:
            return False
        d,n={},len(s)
        for w in wordDict:
            d[w]=1
        dp=[False]*(n+1)
        dp[0]=True
        for i in range(1,n+1):          # Iterate backpack first since permutation
            for j in range(i):
                if dp[j] and s[j:i] in d:
                    dp[i]=True
        return dp[n]


    # Backtrack with memoization
    def wordBreakBM(self, s: str, wordDict: List[str]) -> bool:

        def backtrack(startIndex):
            if startIndex>=n:
                return True
            if not mem[startIndex]:
                return False
            for i in range(startIndex, n):
                cur=s[startIndex:i+1]
                if cur in d:
                    if backtrack(i+1):
                        return True
            mem[startIndex]=False
            return False

        if not s or not wordDict:
            return False
        d,n={},len(s)
        mem=[1]*n
        for w in wordDict:
            d[w]=1
        r=backtrack(startIndex=0)
        return r

import unittest

class TestSolution(unittest.TestCase):
    def testWordBreak(self):
        s = Solution()
        # self.assertEqual(s.wordBreak(s = "leetcode", wordDict = ["leet","code"]), True)
        # self.assertEqual(s.wordBreak(s = "applepenapple", wordDict = ["apple","pen"]), True)
        self.assertEqual(s.wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]), False)
        # self.assertEqual(s.wordBreak(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]), False)



if __name__ == '__main__':
    unittest.main()