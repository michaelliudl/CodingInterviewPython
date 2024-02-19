from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        if not nums: return 0
        uniques = set(nums)
        n,m = len(nums),len(uniques)
        curMap = {}
        curCount,left,ans = 0,0,0
        for i in range(n):
            cur = nums[i]
            if cur not in curMap:
                curMap[cur] = 1
                curCount += 1
            else:
                curMap[cur] += 1
            while curCount == m:
                winOut = nums[left]
                curMap[winOut] -= 1
                if curMap[winOut] == 0:
                    del curMap[winOut]
                    curCount -= 1
                left += 1
            # When current substring has all unique values,
            # substrings start from 0 to left-1 all have all unique values
            ans += left
        return ans

import unittest

class TestSolution(unittest.TestCase):
    def testCountCompleteSubarrays(self):
        s = Solution()
        self.assertEqual(s.countCompleteSubarrays(nums = [5,5,5,5]), 10)
        self.assertEqual(s.countCompleteSubarrays(nums = [1,3,1,2,2]), 4)


if __name__ == '__main__':
    unittest.main()