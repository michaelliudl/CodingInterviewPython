from typing import List

class Solution:

    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        if numBottles <= 0 or numExchange <= 0:
            return 0
        result = numBottles
        empty = numBottles
        while empty >= numExchange:
            empty -= numExchange
            result += 1
            empty += 1
            numExchange += 1
        return result



import unittest

class TestSolution(unittest.TestCase):
    def testbulbSwitch(self):
        s = Solution()
        self.assertEqual(s.bulbSwitch(3), 1)
        self.assertEqual(s.bulbSwitch(0), 0)
        self.assertEqual(s.bulbSwitch(1), 1)


if __name__ == '__main__':
    unittest.main()