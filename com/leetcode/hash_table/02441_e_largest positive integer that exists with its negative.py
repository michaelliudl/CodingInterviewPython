from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        pos = set(num for num in nums if num > 0)
        neg = set(num for num in nums if num < 0)
        res = -1
        for num in pos:
            if -num in neg and num > res:
                res = num
        return res


import unittest

class TestSolution(unittest.TestCase):
    def testIsIsomorphic(self):
        s = Solution()
        self.assertEqual(s.isIsomorphic(s = "egg", t = "add"), True)
        self.assertEqual(s.isIsomorphic(s = "foo", t = "bar"), False)
        self.assertEqual(s.isIsomorphic(s = "paper", t = "title"), True)
        self.assertEqual(s.isIsomorphic(s = "badc", t = "baba"), False)
        


if __name__ == '__main__':
    unittest.main()