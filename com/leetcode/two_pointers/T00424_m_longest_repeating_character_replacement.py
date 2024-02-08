from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s: return 0
        decr,prevStart,firstDiffIndex,ans=k,0,0,0
        diffSet=False
        curIndex,curChar=0,None
        while curIndex < len(s):
            if not curChar: 
                curChar=s[curIndex]
            elif s[curIndex]!=curChar and decr>0:
                decr-=1
                if not diffSet:
                    firstDiffIndex=curIndex
            elif s[curIndex]!=curChar and decr==0:
                ans=max(ans, (curIndex-prevStart))
                curIndex=prevStart=firstDiffIndex
                curChar=None
                decr=k
            curIndex+=1
        ans=max(ans, (curIndex-prevStart))
        return ans



import unittest

class TestSolution(unittest.TestCase):
    def testCharacterReplacement(self):
        s = Solution()
        self.assertEqual(s.characterReplacement(s = "AAAB", k = 0), 3)
        self.assertEqual(s.characterReplacement(s = "ABAB", k = 2), 4)
        self.assertEqual(s.characterReplacement(s = "AABABBA", k = 1), 4)


if __name__ == '__main__':
    unittest.main()