from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backtrack(nums, startIndex, r, path):
            if startIndex>=len(nums):
                return
            for i in range(startIndex, len(nums)):
                path.append(nums[i])
                r.append(path[:])
                backtrack(nums, i+1, r, path)
                path.pop()

        if not nums:
            return []
        r=[[]]
        backtrack(nums, startIndex=0, r=r, path=[])
        return r

import unittest

class TestSolution(unittest.TestCase):
    def testSubsets(self):
        s = Solution()
        self.assertEqual(s.subsets(nums = [1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        self.assertEqual(s.subsets(nums = [0]), [[],[0]])
        


if __name__ == '__main__':
    unittest.main()