from typing import List
import math

class Solution:

    def numSteps(self, s: str) -> int:
        res = carry = 0
        for i in range(len(s) - 1, 0, -1):
            digit = (int(s[i]) + carry) % 2
            if digit == 1:
                carry = 1
            res += 1
        res += carry
        return res

    # Simulate, O(n**2)
    def numStepsSim(self, s: str) -> int:

        def addOne(s):
            index = len(s) - 1
            sList = list(s)
            while index >= 0 and sList[index] == '1':
                sList[index] = '0'
                index -= 1
            if index == -1:
                sList = ['1'] + sList
            else:
                sList[index] = '1'
            return ''.join(sList)

        res = 0
        while s != '1':
            if s[-1] == '0':
                s = s[:-1]
            else:
                s = addOne(s)
            res += 1
        return res


import unittest

class TestSolution(unittest.TestCase):
    def testCanJump(self):
        s = Solution()
        self.assertEqual(s.canJump(nums = [2,3,1,1,4]), True)
        self.assertEqual(s.canJump(nums = [3,2,1,0,4]), False)
        


if __name__ == '__main__':
    unittest.main()