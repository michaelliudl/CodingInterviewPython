from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        if not s or len(s)<2:
            return None
        i,j=0,len(s)-1
        while i<j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        return None

import unittest

class TestSolution(unittest.TestCase):
    def testReverseString(self):
        s = Solution()
        s1 = ["h","e","l","l","o"]
        s.reverseString(s1)
        self.assertEqual(s1, ["o","l","l","e","h"])

        s2 = ["H","a","n","n","a","h"]
        s.reverseString(s2)
        self.assertEqual(s2, ["h","a","n","n","a","H"])


if __name__ == '__main__':
    unittest.main()