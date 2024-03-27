from typing import List

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        
        def bad():
            for _, count in counts.items():
                if count > 2:
                    return True
            return False
        
        if not s:
            return 0
        left = 0
        counts = {}
        result = 0
        for i in range(len(s)):
            counts[s[i]] = counts.get(s[i], 0) + 1
            while bad():
                counts[s[left]] -= 1
                left += 1
            result = max(result, i - left + 1)
        return result

import unittest

class TestSolution(unittest.TestCase):
    def testMaximumLengthSubstring(self):
        s = Solution()
        self.assertEqual(s.maximumLengthSubstring(s = "bcbbbcba"), 4)
        self.assertEqual(s.maximumLengthSubstring(s = "aaaa"), 2)


if __name__ == '__main__':
    unittest.main()