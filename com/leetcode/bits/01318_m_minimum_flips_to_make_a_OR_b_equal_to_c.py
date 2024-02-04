from typing import Optional,List,Deque


class Solution:

    def minFlips(self, a: int, b: int, c: int) -> int:
        ans=0
        while a>0 or b>0 or c>0:
            if c & 1 == 1:
                if a & 1 == 0 and b & 1 == 0:
                    ans += 1
            else:
                if a & 1 == 1 and b & 1 == 1:
                    ans += 2
                elif a & 1 == 1 or b & 1 == 1:
                    ans += 1
            a >>= 1
            b >>= 1
            c >>= 1
        return ans


import unittest

class TestSolution(unittest.TestCase):
    def testMinFlips(self):
        s = Solution()
        self.assertEqual(s.minFlips(a = 8, b = 3, c = 5), 3)
        self.assertEqual(s.minFlips(a = 2, b = 6, c = 5), 3)
        self.assertEqual(s.minFlips(a = 4, b = 2, c = 7), 1)
        self.assertEqual(s.minFlips(a = 1, b = 2, c = 3), 0)

if __name__ == '__main__':
    unittest.main()