from typing import List
import random

class Solution:

    # Since array length is n and elements are in range [1,n], and duplicates by exactly 2,
    # Use array element at (current element - 1) index as flag, turn it to negative at first time
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        result = []
        for i in range(len(nums)):
            flagIndex = abs(nums[i]) - 1        # Take abs since it could be used as negative flag by other elements
            if nums[flagIndex] < 0:
                result.append(abs(nums[i]))
            else:
                nums[flagIndex] = -nums[flagIndex]
        return result

import unittest

class TestSolution(unittest.TestCase):

    def testFindDuplicates(self):
        s=Solution()
        self.assertEqual(s.findDuplicates(nums = [4,3,2,7,8,2,3,1]), [2,3])
        self.assertEqual(s.findDuplicates(nums = [1,1,2]), [1])
        self.assertEqual(s.findDuplicates(nums = [1]), [])

if __name__ == '__main__':
    unittest.main()