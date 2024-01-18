from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, visited, r, path):
            if len(path)==len(nums):
                r.append(path[:])
                return
            for i,v in enumerate(nums):
                if i>0 and nums[i]==nums[i-1] and not visited[i-1]:
                    continue
                if visited[i]:
                    continue

                visited[i]=True
                path.append(v)
                backtrack(nums, visited, r, path)
                path.pop()
                visited[i]=False


        if not nums:
            return []
        r=[]
        nums=sorted(nums)
        backtrack(nums, visited=[False]*len(nums), r=r, path=[])
        return r

import unittest

class TestSolution(unittest.TestCase):
    def testSubsets(self):
        s = Solution()
        self.assertEqual(s.subsets(nums = [1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        self.assertEqual(s.subsets(nums = [0]), [[],[0]])
        


if __name__ == '__main__':
    unittest.main()