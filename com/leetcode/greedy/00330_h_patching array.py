from typing import List,Optional

class Solution:

    def minPatches(self, nums: List[int], n: int) -> int:
        res = 0
        i = 0
        missingNum = 1      # Current smallest number possibly missing from [1, n]

        while missingNum <= n:
            if i < len(nums) and nums[i] <= missingNum:
                missingNum += nums[i]
                i += 1
            else:
                missingNum *= 2     # Greedily double `missingNum`
                res += 1
        return res


import unittest

class TestSolution(unittest.TestCase):
    def testMinPatches(self):
        s = Solution()
        self.assertEqual(s.minPatches(nums = [1,3], n = 6), 1)
        self.assertEqual(s.minPatches(nums = [1,5,10], n = 20), 2)
        self.assertEqual(s.minPatches(nums = [1,2,2], n = 5), 0)
        


if __name__ == '__main__':
    unittest.main()