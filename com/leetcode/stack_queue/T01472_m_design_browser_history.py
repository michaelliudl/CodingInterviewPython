from typing import List

class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack=[homepage]
        self.pos=0
        self.cap=0

    def visit(self, url: str) -> None:
        for i in range(self.pos+1, self.cap+1):
            self.stack[i]=None
        self.pos+=1
        self.cap=self.pos
        if self.pos>=len(self.stack):
            self.stack.append(url)
        else:
            self.stack[self.pos]=url

    def back(self, steps: int) -> str:
        allowed=min(self.pos, steps)
        nextPos=self.pos-allowed
        self.pos=nextPos
        return self.stack[self.pos]

    def forward(self, steps: int) -> str:
        allowed=min((self.cap-self.pos),steps)
        nextPos=self.pos+allowed
        self.pos=nextPos
        return self.stack[self.pos]

class Solution:
    pass


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