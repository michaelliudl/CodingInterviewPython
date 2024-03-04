from typing import List

class Solution:

    def maximumOddBinaryNumber(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        left, n = 0, len(s)
        s_arr = list(s)
        for i in range(n-1):
            if s_arr[i] == '1':
                if s_arr[-1] == '0':
                    s_arr[i], s_arr[-1] = s_arr[-1], s_arr[i]
                elif left < i and s_arr[left] == '0':
                    s_arr[i], s_arr[left] = s_arr[left], s_arr[i]
            if s_arr[left] == '1':
                left += 1
        return ''.join(s_arr)


        

import unittest

class TestSolution(unittest.TestCase):

    def testPivotIndex(self):
        s=Solution()
        self.assertEqual(s.pivotIndex(nums = [1,7,3,6,5,6]), 3)
        self.assertEqual(s.pivotIndex(nums = [2,1,-1]), 0)
        self.assertEqual(s.pivotIndex(nums = [1,2,3]), -1)

if __name__ == '__main__':
    unittest.main()