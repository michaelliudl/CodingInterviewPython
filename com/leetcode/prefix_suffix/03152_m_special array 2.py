from typing import List

class Solution:

    # Assign elements into parity groups, then check if query range falls into the same group
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        parityGroup = 0
        groups = [0] * len(nums)
        for i in range(1, len(nums)):
            if (nums[i - 1] & 1) == (nums[i] & 1):
                parityGroup += 1
            groups[i] = parityGroup
        res = [False] * len(queries)
        for index, [start, end] in enumerate(queries):
            res[index] = (groups[start] == groups[end])
        return res
        

import unittest

class TestSolution(unittest.TestCase):

    def testInsert(self):
        s=Solution()
        self.assertEqual(s.insert(intervals = [], newInterval = [5,7]), [[5,7]])
        self.assertEqual(s.insert(intervals = [[1,3],[6,9]], newInterval = [2,5]), [[1,5],[6,9]])
        self.assertEqual(s.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]), [[1,2],[3,10],[12,16]])

if __name__ == '__main__':
    unittest.main()