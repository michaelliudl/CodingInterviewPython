from typing import List
import heapq
import random

class Solution:

    # Sort, then loop sorted and increment start index when another element is greater
    def maximizeGreatness(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        index = 0
        for num in nums:
            if num > nums[index]:
                index += 1
        return index

import unittest

class TestSolution(unittest.TestCase):
    def testSortArray(self):
        s = Solution()
        self.assertEqual(s.sortArray(nums = [5,2,3,1]), [1,2,3,5])
        self.assertEqual(s.sortArray(nums = [5,1,1,2,0,0]), [0,0,1,1,2,5])


if __name__ == '__main__':
    unittest.main()