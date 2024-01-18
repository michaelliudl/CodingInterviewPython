from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, visited, r, path):
            if len(path)==len(nums):
                r.append(path[:])
                return
            for i,v in enumerate(nums):
                if 1<<i & visited:
                    continue
                visited ^= 1<<i
                path.append(v)
                backtrack(nums, visited, r, path)
                path.pop()
                visited ^= 1<<i


        if not nums:
            return []
        r=[]
        backtrack(nums, visited=0, r=r, path=[])
        return r


import unittest

class TestSolution(unittest.TestCase):
    def testSubsets(self):
        s = Solution()
        self.assertEqual(s.subsets(nums = [1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        self.assertEqual(s.subsets(nums = [0]), [[],[0]])
        


if __name__ == '__main__':
    unittest.main()