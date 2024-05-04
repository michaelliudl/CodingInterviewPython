from typing import List

class Solution:

    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch)
        if index >= 0:
            pre = list(word[:index+1])
            pre.reverse()
            return ''.join(pre) + word[index+1:]
        return word


import unittest

class TestSolution(unittest.TestCase):
    def testMakeGood(self):
        s = Solution()
        self.assertEqual(s.makeGood(s = "leEeetcode"), "leetcode")
        self.assertEqual(s.makeGood(s = "abBAcC"), "")
        self.assertEqual(s.makeGood(s = "s"), "s")
        

if __name__ == '__main__':
    unittest.main()