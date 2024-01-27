from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pass

import unittest

class TestSolution(unittest.TestCase):
    def testIsPalindrome(self):
        s = Solution()
        self.assertEqual(s.isPalindrome(s = "A man, a plan, a canal: Panama"), True)
        self.assertEqual(s.isPalindrome(s = "race a car"), False)
        self.assertEqual(s.isPalindrome(" "), True)


if __name__ == '__main__':
    unittest.main()