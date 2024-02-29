from typing import List

class Solution:

    def numberToWords(self, num: int) -> str:
        pass

import unittest

class TestSolution(unittest.TestCase):
    def testbulbSwitch(self):
        s = Solution()
        self.assertEqual(s.bulbSwitch(3), 1)
        self.assertEqual(s.bulbSwitch(0), 0)
        self.assertEqual(s.bulbSwitch(1), 1)


if __name__ == '__main__':
    unittest.main()