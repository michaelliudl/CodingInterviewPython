from typing import List

class Solution:

    def makeGood(self, s: str) -> str:

        def bad(prev, char):
            prevLower, prevDiff = check(prev)
            charLower, charDiff = check(char)
            return ((prevLower and not charLower) or (not prevLower and charLower)) and prevDiff == charDiff
        
        def check(char):
            isLower = 'a' <= char <= 'z'
            diff = ord(char) - (ord('a') if isLower else ord('A'))
            return isLower, diff

        if not s:
            return s
        sList = list(s)
        while sList:
            newList = []
            prev = None
            for char in sList:
                if not prev:
                    prev = char
                    continue
                elif bad(prev, char):
                    prev = None
                else:
                    newList.append(prev)
                    prev = char
            if prev:
                newList.append(prev)
            if newList == sList:
                break
            sList = newList
        return ''.join(sList)


import unittest

class TestSolution(unittest.TestCase):
    def testMakeGood(self):
        s = Solution()
        self.assertEqual(s.makeGood(s = "leEeetcode"), "leetcode")
        self.assertEqual(s.makeGood(s = "abBAcC"), "")
        self.assertEqual(s.makeGood(s = "s"), "s")
        

if __name__ == '__main__':
    unittest.main()