from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums: return True
        d={}
        for num in nums:
            if num in d: return True
            d[num]=1
        return False


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