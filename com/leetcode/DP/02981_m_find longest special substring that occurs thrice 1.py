from typing import List

class Solution:

    # Count continuous occurrences of each character
    # Then find maximum continuous length of each character that occurred at least 3 times
    def maximumLength(self, s: str) -> int:

        # Get max continous length of the character that occurred at 3 times
        def getMaxFreq(count):
            freq = 0
            for i in range(n, 0, -1):   # Start from largest possible continuous length
                freq += count[i]
                if freq >= 3:
                    return i
            return -1   # -1 if no character occurs at 3 times

        n = len(s)
        continuousLen = 0
        curChar = None
        # Count each character's occurrences of continuous 1-n times
        counts = [[0] * (n + 1) for _ in range(26)]
        for char in s:
            if not curChar or char != curChar:
                curChar = char
                continuousLen = 1
            else:
                continuousLen += 1
            counts[ord(char) - ord('a')][continuousLen] += 1
        return max(getMaxFreq(count) for count in counts)
    

import unittest

class TestSolution(unittest.TestCase):
    def testMaximumLength(self):
        s = Solution()
        self.assertEqual(s.maximumLength(s = "aaaa"), 2)
        self.assertEqual(s.maximumLength(s = "abcdef"), -1)
        self.assertEqual(s.maximumLength(s = "abcaba"), 1)


if __name__ == '__main__':
    unittest.main()