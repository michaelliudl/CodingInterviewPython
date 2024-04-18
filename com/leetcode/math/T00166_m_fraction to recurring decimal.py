from typing import List

class Solution:

    # How to determine division result is infinite repeating or non infinite repeating like 0.55
    # How to find first repeating number after `.`, like 0.16666666
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator / denominator == numerator // denominator:
            return str(numerator // denominator)
        decimal = str(numerator / denominator)
        result = []
        startNum = ''
        dotIndex = -1
        repeat = False
        for index, char in enumerate(decimal):
            if char != '.' and dotIndex < 0:
                result.append(char)
            elif char == '.':
                result.append(char)
                dotIndex = index
            elif not startNum:
                startNum = decimal[index]
            elif decimal[index] == startNum:
                repeat = True
                result.append('(')
                result.append(decimal[dotIndex + 1:index])
                result.append(')')
                break
        if not repeat:
            result.append(decimal[dotIndex + 1:])
        return ''.join(result)


import unittest

class TestSolution(unittest.TestCase):
    def testFractionToDecimal(self):
        s = Solution()
        self.assertEqual(s.fractionToDecimal(numerator = 1, denominator = 6), "0.1(6)")
        self.assertEqual(s.fractionToDecimal(numerator = 4, denominator = 333), "0.(012)")
        self.assertEqual(s.fractionToDecimal(numerator = 1, denominator = 2), "0.5")
        self.assertEqual(s.fractionToDecimal(numerator = 2, denominator = 1), "2")


if __name__ == '__main__':
    unittest.main()