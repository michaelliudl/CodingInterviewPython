from typing import List

class Solution:

    # Sliding window count
    def findAnagrams(self, s: str, p: str) -> List[int]:

        def eq(cache, window):
            for c in window:
                if c not in cache or window[c] != cache[c]:
                    return False
            return True

        if not s or not p: return []
        m,n=len(s),len(p)
        if m<n: return []
        cache={}
        for c in p:
            cache[c] = cache.get(c, 0) + 1

        window={}
        ans=[]
        for i in range(n):
            c = s[i]
            window[c] = window.get(c, 0) + 1
        if eq(cache, window): ans.append(0)

        for i in range(n, m):   # i is end of current window
            winIn, winOut = s[i], s[i - n]
            window[winIn] = window.get(winIn, 0) + 1
            window[winOut]-=1
            if window[winOut] == 0: del window[winOut]
            if eq(cache, window): ans.append(i - n + 1)
        return ans

import unittest

class TestSolution(unittest.TestCase):
    def testFindAnagrams(self):
        s = Solution()
        self.assertEqual(s.findAnagrams(s = "aaaaaaaaaa", p = "aaaaaaaaaaaaa"), [])
        self.assertEqual(s.findAnagrams(s = "baa", p = "aa"), [1])
        self.assertEqual(s.findAnagrams(s = "cbaebabacd", p = "abc"), [0,6])
        self.assertEqual(s.findAnagrams(s = "abab", p = "ab"), [0,1,2])


if __name__ == '__main__':
    unittest.main()