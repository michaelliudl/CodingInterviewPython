from typing import List

class Solution:

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        def backtrack(nums, startIndex, r, path):
            if startIndex>=len(nums):
                return
            # Unordered array
            # 1. Use dict to dedup
            # d={}
            # 2. Use array to dedup, elements [-100,100]
            # d=[0]*201
            # 3. Use bit
            d=0
            for i in range(startIndex, len(nums)):
                cur=nums[i]
                # 1. Dict Check
                # if cur in d:
                #     continue
                # else:
                #     d[cur]=1
                # 2. Array Check
                # if d[cur]==1:
                #     continue
                # else:
                #     d[cur]=1
                # 3. Bit check
                shift=cur if cur>=0 else (100-cur)
                if 1<<shift & d:
                    continue
                else:
                    d |= 1<<shift
                if not path or cur>=path[-1]:
                    path.append(cur)
                if cur<path[-1]:
                    continue
                if len(path)>1:
                    r.append(path[:])
                backtrack(nums, startIndex=i+1, r=r, path=path)
                path.pop()

        if not nums:
            return []
        r=[]
        backtrack(nums, startIndex=0, r=r, path=[])
        return r

import unittest

class TestSolution(unittest.TestCase):
    def testFindSubsequences(self):
        s = Solution()
        self.assertEqual(s.findSubsequences(nums = [4,6,7,7]), [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]])
        self.assertEqual(s.findSubsequences(nums = [4,4,3,2,1]), [[4,4]])
        


if __name__ == '__main__':
    unittest.main()