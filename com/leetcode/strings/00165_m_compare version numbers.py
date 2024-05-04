from typing import List

class Solution:

    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = [int(v) for v in version1.split('.')]
        ver2 = [int(v) for v in version2.split('.')]
        longer = max(len(ver1), len(ver2))
        while len(ver1) < longer:
            ver1.append(0)
        while len(ver2) < longer:
            ver2.append(0)
        for i in range(longer):
            if ver1[i] < ver2[i]:
                return -1
            elif ver1[i] > ver2[i]:
                return 1
        return 0

import unittest

class TestSolution(unittest.TestCase):
    def testMyAtoi(self):
        s = Solution()
        self.assertEqual(s.myAtoi(s = "   +0 123"), 0)
        self.assertEqual(s.myAtoi(s = "00000-42a1234"), 0)
        self.assertEqual(s.myAtoi(s = "   -42"), -42)
        self.assertEqual(s.myAtoi(s = "42"), 42)
        self.assertEqual(s.myAtoi(s = "+-12"), 0)
        self.assertEqual(s.myAtoi(s = "words and 987"), 0)
        self.assertEqual(s.myAtoi(s = "4193 with words"), 4193)
        

if __name__ == '__main__':
    unittest.main()