from typing import List, Counter

class Solution:

    # Constant size moving window
    def checkInclusion(self, s1: str, s2: str) -> bool:
        subStrCharCounts = Counter(s1)
        requiredLen = len(s1)
        for index, char in enumerate(s2):
            subStrCharCounts[char] -= 1
            if subStrCharCounts[char] >= 0:
                requiredLen -= 1
            if index >= len(s1):
                subStrCharCounts[s2[index - len(s1)]] += 1
                if subStrCharCounts[s2[index - len(s1)]] > 0:
                    requiredLen += 1
            if requiredLen == 0:
                return True
        return False

    # Classic sliding window
    def checkInclusionClassic(self, s1: str, s2: str) -> bool:
        subStrCharCounts = [0] * 26
        for char in s1:
            subStrCharCounts[ord(char) - ord('a')] += 1
        requiredLen = len(s1)
        left = 0
        for index, char in enumerate(s2):
            subStrCharCounts[ord(char) - ord('a')] -= 1
            if subStrCharCounts[ord(char) - ord('a')] >= 0:
                requiredLen -= 1
            while requiredLen == 0:
                if index - left + 1 == len(s1):
                    return True
                subStrCharCounts[ord(s2[left]) - ord('a')] += 1
                if subStrCharCounts[ord(s2[left]) - ord('a')] > 0:
                    requiredLen += 1
                left += 1
        return False

import unittest

class TestSolution(unittest.TestCase):
    def testminWindow(self):
        s = Solution()
        self.assertEqual(s.minWindow(s = "ADOBECODEBANC", t = "ABC"), "BANC")
        self.assertEqual(s.minWindow(s = "a", t = "a"), 'a')
        self.assertEqual(s.minWindow(s = "a", t = "aa"), '')


if __name__ == '__main__':
    unittest.main()