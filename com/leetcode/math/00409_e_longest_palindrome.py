from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s: return 0
        d={}
        for c in s:
            if c in d: d[c]+=1
            else: d[c]=1
        ans,hasOdd=0,False
        for _,v in d.items():
            if v%2==0: ans+=v
            else:
                hasOdd=True
                ans+=(v-1)
        return ans+1 if hasOdd else ans

import unittest

class TestSolution(unittest.TestCase):
    def testThreeSum(self):
        s = Solution()
        self.assertEqual(s.threeSum([-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]])
        self.assertEqual(s.threeSum([0,1,1]), [])
        self.assertEqual(s.threeSum([0,0,0]), [[0,0,0]])


if __name__ == '__main__':
    unittest.main()