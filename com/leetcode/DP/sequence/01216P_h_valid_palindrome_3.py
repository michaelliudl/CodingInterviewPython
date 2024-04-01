from typing import List, Deque

'''
Given a string s and an integer k, return true if s is a k-palindrome.

A string is k-palindrome if it can be transformed into a palindrome by removing at most k characters from it.

'''
class Solution:

    # Find longest palindrome subsequence as 516
    def isValidPalindrome(self, s: str, k: int) -> bool:

        def longestPalinSubseq(string):
            dp = [[0] * n for _ in range(n)]
            for i in range(n - 1, -1, -1):
                for j in range(i, n):
                    if i == j:
                        dp[i][j] = 1
                    elif s[i] == s[j]:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                    else:
                        dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
            return dp[0][n - 1]

        if not s:
            return True
        n = len(s)
        lps = longestPalinSubseq(s)
        return lps >= (n - k)

    # Try to use BFS like 301, MLE on s = "baaccaacbdcadbcdacbbdabbdddabdddadcabbdbbcaadbbdcbddcbdcdbaadaab", k = 9
    def isValidPalindromeBFS(self, s: str, k: int) -> bool:
        
        def isPalin(string):
            low, high = 0, len(string) - 1
            while low < high:
                if string[low] != string[high]:
                    return False
                low += 1
                high -= 1
            return True
        
        if not s:
            return True
        if k <= 0:
            return isPalin(s)
        queue = Deque()
        queue.append(s)
        used = set()
        used.add(s)
        level = 0
        while queue and level <= k:
            curLen = len(queue)
            for _ in range(curLen):
                cur = queue.popleft()
                if isPalin(cur):
                    return True
                if level == k:
                    continue
                for i in range(len(cur)):
                    nextStr = cur[:i] + cur[i+1:]
                    if nextStr not in used:
                        used.add(nextStr)
                        queue.append(nextStr)
            level += 1
        return False

import unittest

class TestSolution(unittest.TestCase):
    def testIsValidPalindrome(self):
        s = Solution()
        self.assertEqual(s.isValidPalindrome(s = "abcdeca", k = 2), True)
        self.assertEqual(s.isValidPalindrome(s = "abbababa", k = 1), True)
        self.assertEqual(s.isValidPalindrome(s = "baaccaacbdcadbcdacbbdabbdddabdddadcabbdbbcaadbbdcbddcbdcdbaadaab", k = 9), False)
        


if __name__ == '__main__':
    unittest.main()