from typing import List

class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, startIndex, r, path):
            if startIndex>=len(nums):
                return
            for i in range(startIndex, len(nums)):
                if i>startIndex and nums[i]==nums[i-1]:
                    continue
                path.append(nums[i])
                r.append(path[:])
                backtrack(nums, i+1, r, path)
                path.pop()
        
        if not nums:
            return []
        nums=sorted(nums)
        r=[[]]
        backtrack(nums, startIndex=0, r=r, path=[])
        return r

import unittest

class TestSolution(unittest.TestCase):
    def testSubsetsWithDup(self):
        s = Solution()
        self.assertEqual(s.subsetsWithDup(nums = [1,2,2]), [[],[1],[1,2],[1,2,2],[2],[2,2]])
        self.assertEqual(s.subsetsWithDup(nums = [0]), [[],[0]])
        


if __name__ == '__main__':
    unittest.main()