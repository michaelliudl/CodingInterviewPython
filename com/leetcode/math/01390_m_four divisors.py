from typing import List
import math

class Solution:

    def sumFourDivisors(self, nums: List[int]) -> int:

        def getDivs(num):
            divs = set()
            divs.add(1)
            divs.add(num)
            for i in range(2, int(math.sqrt(num)) + 1): # Up to square root of the number
                if num % i == 0:
                    divs.add(i)
                    divs.add(num // i)
            return divs

        if not nums:
            return 0
        result = 0
        for num in nums:
            divs = getDivs(num)
            if len(divs) == 4:
                result += sum(divs)
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