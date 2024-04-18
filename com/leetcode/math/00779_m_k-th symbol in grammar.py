from typing import List

class Solution:

    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return 0 if k == 1 else 1
        prevK = (k // 2) if (k % 2 == 0) else (k // 2 + 1)
        prev = self.kthGrammar(n - 1, prevK)
        if (prev == 0 and k % 2 == 0) or (prev == 1 and k % 2 == 1):
            return 1
        else:
            return 0



import unittest

class TestSolution(unittest.TestCase):
    def testbulbSwitch(self):
        s = Solution()
        self.assertEqual(s.bulbSwitch(3), 1)
        self.assertEqual(s.bulbSwitch(0), 0)
        self.assertEqual(s.bulbSwitch(1), 1)


if __name__ == '__main__':
    unittest.main()