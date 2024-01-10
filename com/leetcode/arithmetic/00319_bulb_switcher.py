from typing import List

class Solution:

    '''
    Initially, all bulbs are off.
    In the i-th round, we toggle every i-th bulb.
    A bulb ends up on only if it is toggled an odd number of times.
    Bulbs are toggled when their factors are encountered (e.g., the 12th bulb is toggled at rounds 1, 2, 3, 4, 6, and 12).
    For each bulb, the number of its factors indicates how many times it will be toggled.
    Only perfect squares have an odd number of factors (except 1, which has a single factor).

    Therefore, the number of bulbs that will be on after n rounds is equal to the number of perfect squares less than or equal to n. 
    This is achieved by taking the square root of n and converting it to an integer.
    '''

    def bulbSwitch(self, n: int) -> int:
        return int(n**0.5)
        

    def bulbSwitchBrute(self, n: int) -> int:
        if n<=1:
            return n
        b=[1]*n
        for i in range(2,n):
            for j in range(i-1,n,i):
                b[j]=1 if b[j]==0 else 0
        b[n-1]=1 if b[n-1]==0 else 0
        return sum(b)
        

import unittest

class TestSolution(unittest.TestCase):
    def testbulbSwitch(self):
        s = Solution()
        self.assertEqual(s.bulbSwitch(3), 1)
        self.assertEqual(s.bulbSwitch(0), 0)
        self.assertEqual(s.bulbSwitch(1), 1)


if __name__ == '__main__':
    unittest.main()