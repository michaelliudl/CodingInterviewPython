from typing import List
from typing import Deque


class Solution:

    def removeKdigits(self, num: str, k: int) -> str:
        if not num:
            return ''
        if k >= len(num):
            return '0'
        result = float('inf')
        for i in range(k, len(num) + 1):
            removed = num[:(i - k)] + num[i:]
            result = min(result, int(removed))
        return str(result)



import unittest

class TestSolution(unittest.TestCase):
    def testRemoveKdigits(self):
        s = Solution()
        self.assertEqual(s.removeKdigits(num = "1432219", k = 3), '1219')
        self.assertEqual(s.removeKdigits(num = "10200", k = 1), '200')
        self.assertEqual(s.removeKdigits(num = "10", k = 2), '0')
        self.assertEqual(s.removeKdigits(num = "112", k = 1), '11')
        self.assertEqual(s.removeKdigits(num = "10001", k = 1), '0')



if __name__ == '__main__':
    unittest.main()