
''' Given a string s, return true if a permutation of the string could form a 
palindrome
 and false otherwise.
'''
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if not s:
            return True
        charMap = {}
        for char in s:
            charMap[char] = charMap.get(char, 0) + 1
        odd = 0
        for _, count in charMap.items():
            if count % 2 == 1:
                odd += 1
                if odd > 1:
                    return False
        return odd <= 1


import unittest

class TestSolution(unittest.TestCase):
    def testMinAddToMakeValid(self):
        s = Solution()
        self.assertEqual(s.minAddToMakeValid("())"), 1)
        self.assertEqual(s.minAddToMakeValid("((("), 3)


if __name__ == '__main__':
    unittest.main()