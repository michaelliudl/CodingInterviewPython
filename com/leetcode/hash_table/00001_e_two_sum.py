from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums)<2:
            return None
        d=dict()
        for i in range(len(nums)):
            d[nums[i]]=i
        l=list()
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in d and d[diff]!=i:
                l.append(i)
                l.append(d[diff])
                return l
        return None

import unittest

class TestSolution(unittest.TestCase):
    def testTwoSum(self):
        s = Solution()
        self.assertEqual(s.twoSum([2,7,11,15],9), [0,1])
        self.assertEqual(s.twoSum([3,2,4],6), [1,2])
        self.assertEqual(s.twoSum([3,3],6), [0,1])


if __name__ == '__main__':
    unittest.main()