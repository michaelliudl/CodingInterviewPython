from typing import List

class Solution:

    def uniqueLetterString(self, s: str) -> int:
        if not s:
            return 0
        # dp is the number of unique letters in all substrings ending at the current index
        dp = 0
        lastCount = {}
        lastSeen = {}
        result = 0
        for index, char in enumerate(s):
            newCount = index - lastSeen.get(char, -1)
            # Subtract duplicates
            dp -= lastCount.get(char, 0)
            # Add count of s[lastSeen[char] + 1 .. i], s[lastSeen[char] + 2 .. i], ..., s[i]
            dp += newCount
            lastCount[char] = newCount
            lastSeen[char] = index
            result += dp
        return result


import unittest

class TestSolution(unittest.TestCase):
    def testUniqueLetterString(self):
        s = Solution()
        self.assertEqual(s.uniqueLetterString(s = "ABC"), 10)
        self.assertEqual(s.uniqueLetterString(s = "ABA"), 8)
        self.assertEqual(s.uniqueLetterString(s = "LEETCODE"), 92)


if __name__ == '__main__':
    unittest.main()