from typing import List

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def match(winMap, tMap):
            for k,v in tMap.items():
                if k not in winMap or v > winMap[k]:
                    return False
            return True

        if not s or not t or len(s)<len(t): return ''
        tMap = {}
        for c in t:
            if c not in tMap:
                tMap[c] = 1
            else:
                tMap[c] += 1
        minLen = float('inf')
        n, winStart, winEnd, start = len(s), -1, -1, -1
        winMap = {}
        for i in range(n):
            if s[i] in tMap:
                if start < 0: start = i
                if s[i] in winMap:
                    winMap[s[i]] += 1
                else:
                    winMap[s[i]] = 1
            while match(winMap, tMap):
                curLen = i - start + 1
                if curLen < minLen:
                    minLen = curLen
                    winStart, winEnd = start, i
                winOut = s[start]
                winMap[winOut] -= 1
                if winMap[winOut] == 0: del winMap[winOut]
                for j in range(start + 1, i+1):
                    if s[j] in tMap:
                        start = j
                        break
        return s[winStart : winEnd + 1]

import unittest

class TestSolution(unittest.TestCase):
    def testminWindow(self):
        s = Solution()
        self.assertEqual(s.minWindow(s = "ADOBECODEBANC", t = "ABC"), "BANC")
        self.assertEqual(s.minWindow(s = "a", t = "a"), 'a')
        self.assertEqual(s.minWindow(s = "a", t = "aa"), '')


if __name__ == '__main__':
    unittest.main()