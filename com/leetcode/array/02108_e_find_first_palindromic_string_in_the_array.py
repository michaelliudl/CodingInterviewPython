from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        def isPalin(word):
            left, right = 0, len(word)-1
            while left < right:
                if word[left] == word[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True

        if not words: return ''
        for word in words:
            if isPalin(word):
                return word
        return ''

        

import unittest

class TestSolution(unittest.TestCase):

    def testPivotIndex(self):
        s=Solution()
        self.assertEqual(s.pivotIndex(nums = [1,7,3,6,5,6]), 3)
        self.assertEqual(s.pivotIndex(nums = [2,1,-1]), 0)
        self.assertEqual(s.pivotIndex(nums = [1,2,3]), -1)

if __name__ == '__main__':
    unittest.main()