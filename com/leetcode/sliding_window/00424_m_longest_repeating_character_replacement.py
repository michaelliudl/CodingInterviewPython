from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s: return 0
        left,maxCount,ans=0,0,0
        counter={}
        for right in range(len(s)):
            rightValue=s[right]
            if rightValue in counter:
                counter[rightValue]+=1
            else:
                counter[rightValue]=1
            maxCount = max(maxCount, counter[rightValue])   # Max count of same characters in range
            while (right - left + 1) - maxCount > k:        # (right - left + 1) = Total chars in range
                winOut = s[left]
                counter[winOut] -= 1
                left += 1
            ans=max(ans, (right - left + 1))
        return ans



import unittest

class TestSolution(unittest.TestCase):
    def testCharacterReplacement(self):
        s = Solution()
        self.assertEqual(s.characterReplacement(s = "AABABBA", k = 1), 4)
        self.assertEqual(s.characterReplacement(s = "ABCDE", k = 1), 2)
        self.assertEqual(s.characterReplacement(s = "AAAB", k = 0), 3)
        self.assertEqual(s.characterReplacement(s = "ABAB", k = 2), 4)


if __name__ == '__main__':
    unittest.main()