from typing import List

'''
Given a string s, return the length of the longest 
substring
 that contains at most two distinct characters.
'''

class Solution:

    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not s:
            return 0
        charCount = {}
        left = 0
        result = 0
        for i, char in enumerate(s):
            charCount[char] = charCount.get(char, 0) + 1
            while len(charCount) > 2:
                out = s[left]
                charCount[out] -= 1
                if not charCount[out]:
                    del charCount[out]
                left += 1
            result = max(result, i - left + 1)
        return result

import unittest

class TestSolution(unittest.TestCase):
    def testLengthOfLongestSubstringTwoDistinct(self):
        s = Solution()
        self.assertEqual(s.lengthOfLongestSubstringTwoDistinct(s = "eceba"), 3)
        self.assertEqual(s.lengthOfLongestSubstringTwoDistinct(s = "ccaabbb"), 5)
        

if __name__ == '__main__':
    unittest.main()