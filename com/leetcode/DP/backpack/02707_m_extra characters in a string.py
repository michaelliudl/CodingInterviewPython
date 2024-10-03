from typing import List
import heapq,math

class Solution:

    # Similar to 139 Word Break
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dictSet = set(dictionary)
        dp = [n] * (n + 1)      # dp[i] := min extra characters when splitting s[0..i) optimally
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(i):
                if s[j:i] in dictSet:
                    dp[i] = min(dp[i], dp[j])
                else:
                    dp[i] = min(dp[i], dp[j] + i - j)
        return dp[n]

    # Backtrack with memoization TODO
    def minExtraCharBM(self, s: str, dictionary: List[str]) -> int:

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