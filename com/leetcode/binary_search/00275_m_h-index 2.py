from typing import List

class Solution:

    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        n, hIndex = len(citations), 0
        low, high = 0, n
        while low < high:
            mid = low + (high - low) // 2
            if citations[mid] >= (n - mid):
                hIndex = max(hIndex, (n - mid))
                high = mid
            else:
                low = mid + 1
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