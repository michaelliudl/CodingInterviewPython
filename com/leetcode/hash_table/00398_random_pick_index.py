from typing import List
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.d={}
        if nums:
            for i in range(len(nums)):
                if nums[i] in self.d:
                    self.d[nums[i]].append(i)
                else:
                    self.d[nums[i]]=[i]

    def pick(self, target: int) -> int:
        if target in self.d:
            indices=self.d[target]
            rand=random.randint(0,len(indices)-1)
            return indices[rand]
        return -1

import unittest

class TestSolution(unittest.TestCase):
    def testTwoSum(self):
        s = Solution([1, 2, 3, 3, 3])
        self.assertIn(s.pick(3), [2,3,4])
        self.assertIn(s.pick(1), [0])
        self.assertIn(s.pick(3), [2,3,4])


if __name__ == '__main__':
    unittest.main()