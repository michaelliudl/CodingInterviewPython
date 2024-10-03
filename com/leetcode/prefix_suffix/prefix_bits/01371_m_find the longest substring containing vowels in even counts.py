from typing import Optional,List,Deque

class Solution:

    def findTheLongestSubstring(self, s: str) -> int:
        vowels = 'aeiou'
        res = mask = 0
        maskToIndex = {0: -1}
        for index, char in enumerate(s):
            if char in vowels:
                mask = mask ^ (1 + ord(char) - ord('a'))
            if mask in maskToIndex:
                res = max(res, (index - maskToIndex[mask]))
            else:
                maskToIndex[mask] = index
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testSortByBits(self):
        s = Solution()
        self.assertEqual(s.sortByBits(arr = [0,1,2,3,4,5,6,7,8]), [0,1,2,4,8,3,5,6,7])
        self.assertEqual(s.sortByBits(arr = [1024,512,256,128,64,32,16,8,4,2,1]), [1,2,4,8,16,32,64,128,256,512,1024])

if __name__ == '__main__':
    unittest.main()