from typing import List

class Solution:

    def removeStars(self, s: str) -> str:
        if not s: return s
        arr = []
        for c in s: arr.append(c)
        left = 0
        for i in range(len(arr)):
            if arr[i] == '*':
                if left > 0:
                    left -= 1
            else:
                arr[left] = arr[i]
                left += 1
        return ''.join(arr[:left])

    def removeStarsStack(self, s: str) -> str:
        if not s: return s
        st=[]
        for c in s:
            if c=='*' and st:
                st.pop()
            else:
                st.append(c)
        return ''.join(st)


import unittest

class TestSolution(unittest.TestCase):
    def testBrowserHistory(self):
        s = BrowserHistory('leetcode.com')
        s.visit('google.com')
        s.visit('facebook.com')
        s.visit('youtube.com')
        self.assertEqual(s.back(steps=1), "facebook.com")
        self.assertEqual(s.back(steps=1), "google.com")
        self.assertEqual(s.forward(steps=1), "facebook.com")
        s.visit('linkedin.com')
        self.assertEqual(s.forward(steps=2), "linkedin.com")
        self.assertEqual(s.back(steps=2), "google.com")
        self.assertEqual(s.back(steps=7), "leetcode.com")



if __name__ == '__main__':
    unittest.main()