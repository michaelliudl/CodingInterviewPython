from typing import List

class Solution:

    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        citations.sort()
        n, hIndex = len(citations), 0
        for i in range(n):
            if citations[i] >= (n - i):
                hIndex = max(hIndex, (n - i))
        return hIndex


import unittest

class TestSolution(unittest.TestCase):

    def testCompress(self):
        s = Solution()
        chars = ["a","a","b","b","c","c","c"]
        self.assertEqual(s.compress(chars), 6)
        self.assertEqual(chars[:6], ["a","2","b","2","c","3"])
        chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
        self.assertEqual(s.compress(chars), 4)
        self.assertEqual(chars[:4], ["a","b","1","2"])

if __name__ == '__main__':
    unittest.main()