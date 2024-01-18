from typing import List

class Solution:

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        return max(sum([nums[i] for i in range(len(nums)) if i%2==0]),
                   sum([nums[i] for i in range(len(nums)) if i%2==1]))


import unittest

class TestSolution(unittest.TestCase):
    def testSubsets(self):
        s = Solution()
        self.assertEqual(s.subsets(nums = [1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        self.assertEqual(s.subsets(nums = [0]), [[],[0]])
        


if __name__ == '__main__':
    unittest.main()