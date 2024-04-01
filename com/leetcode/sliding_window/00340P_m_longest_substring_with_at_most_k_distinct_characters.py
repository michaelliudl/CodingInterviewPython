from typing import List

'''
Given a string s and an integer k, return the length of the longest 
substring
 of s that contains at most k distinct characters.
'''
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or k <= 0:
            return 0
        distincts = {}
        left = 0
        result = 0
        for index, char in enumerate(s):
            distincts[char] = distincts.get(char, 0) + 1
            while len(distincts) > k:
                distincts[s[left]] -= 1
                if distincts[s[left]] == 0:
                    del distincts[s[left]]
                left += 1
            result = max(result, index - left + 1)
        return result


import unittest

class TestSolution(unittest.TestCase):
    def testLengthOfLongestSubstringKDistinct(self):
        s = Solution()
        self.assertEqual(s.lengthOfLongestSubstringKDistinct(s = "eceba", k = 2), 3)
        self.assertEqual(s.lengthOfLongestSubstringKDistinct(s = "aa", k = 1), 2)


if __name__ == '__main__':
    unittest.main()