from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        ans,slow=1,0
        d={s[0]: 0}
        for i in range(1,len(s)):
            cur=s[i]
            if cur in d:
                nextSlow=d[cur]+1
                for j in range(slow,nextSlow):
                    del d[s[j]]
                slow=nextSlow
            else:
                ans=max(ans, (i-slow+1))
            d[cur]=i
        return ans


import unittest

class TestSolution(unittest.TestCase):
    def testLengthOfLongestSubstring(self):
        s = Solution()
        self.assertEqual(s.lengthOfLongestSubstring("tmmzuxt"), 5)


if __name__ == '__main__':
    unittest.main()