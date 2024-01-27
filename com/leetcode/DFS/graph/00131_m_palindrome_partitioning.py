from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s: str):
            i,j=0,len(s)-1
            while i<j:
                if s[i]==s[j]:
                    i+=1
                    j-=1
                else:
                    return False
            return True

        def backtrack(s, startIndex, r: List[List[str]], path: List[str]):
            if startIndex>=len(s):
                r.append(path[:])
                return
            for i in range(startIndex, len(s)):
                prefix=s[startIndex:i+1]
                if not isPalindrome(prefix):
                    continue
                path.append(prefix)
                backtrack(s, i+1, r, path)
                path.pop()

        if not s:
            return []
        r=[]
        backtrack(s, 0, r, path=[])
        return r
        

import unittest

class TestSolution(unittest.TestCase):
    def testPartition(self):
        s = Solution()
        self.assertEqual(s.partition(s = "aab"), [["a","a","b"],["aa","b"]])
        self.assertEqual(s.partition(s = "a"), [["a"]])
        


if __name__ == '__main__':
    unittest.main()