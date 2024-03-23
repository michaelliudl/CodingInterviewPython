from typing import List
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    # Loop backwards and swap with random index before i
    def shuffle(self) -> List[int]:
        temp = self.nums[:]
        for i in range(len(temp) - 1, 0, -1):
            j = random.randint(0, i)
            temp[i], temp[j] = temp[j], temp[i]
        return temp
        

import unittest

class TestSolution(unittest.TestCase):

    def testPivotIndex(self):
        s=Solution()
        self.assertEqual(s.pivotIndex(nums = [1,7,3,6,5,6]), 3)
        self.assertEqual(s.pivotIndex(nums = [2,1,-1]), 0)
        self.assertEqual(s.pivotIndex(nums = [1,2,3]), -1)

if __name__ == '__main__':
    unittest.main()