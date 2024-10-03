from typing import List
from typing import Deque
from functools import cmp_to_key

class Solution:

    # Custom sort by comparing numbers from concatenating two strings
    def largestNumber(self, nums: List[int]) -> str:

        def comp(x, y):
            if int(x + y) > int(y + x):
                return -1
            else:
                return 1

        res = ''.join(sorted([str(num) for num in nums], key=cmp_to_key(comp)))
        if res[0] == '0':
            return '0'
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testCarFleet(self):
        s = Solution()
        self.assertEqual(s.carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]), 3)
        self.assertEqual(s.carFleet(target = 10, position = [3], speed = [3]), 1)
        self.assertEqual(s.carFleet(target = 100, position = [0,2,4], speed = [4,2,1]), 1)



if __name__ == '__main__':
    unittest.main()