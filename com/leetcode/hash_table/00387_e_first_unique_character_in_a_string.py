from typing import List

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s: return 0
        map=[0]*26
        for c in s:
            map[ord(c)-ord('a')]+=1
        for i in range(len(s)):
            if map[ord(s[i])-ord('a')]==1: return i
        return -1

import unittest

class TestSolution(unittest.TestCase):
    def testTwoSum(self):
        s = Solution()
        self.assertEqual(s.twoSum([2,7,11,15],9), [0,1])
        self.assertEqual(s.twoSum([3,2,4],6), [1,2])
        self.assertEqual(s.twoSum([3,3],6), [0,1])


if __name__ == '__main__':
    unittest.main()