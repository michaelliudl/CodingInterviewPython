from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        def backtrack():
            nonlocal rem,curSum
            if curSum==subSum:
                curSum=0
                rem-=subSum
                return True
            if curSum>subSum:       # Only positive numbers
                return False
            for i in range(n):
                if not used[i]:
                    used[i]=True
                    curSum+=nums[i]
                    if backtrack():
                        continue
                    else:
                        used[i]=False
                        curSum-=nums[i]
            return True


        if not nums or len(nums)<k: return False
        total=sum(nums)
        if total%k!=0: return False

        subSum=total//k
        n=len(nums)
        used=[0]*n
        rem,curSum=total,0
        backtrack()
        return rem==0 and sum(used)==n

import unittest

class TestSolution(unittest.TestCase):
    def testCanPartitionKSubsets(self):
        s = Solution()
        self.assertEqual(s.canPartitionKSubsets(nums = [1,1,1,1,2,2,2,2], k = 4), True)
        self.assertEqual(s.canPartitionKSubsets(nums = [1,1,1,1,2,2,2,2], k = 2), True)
        self.assertEqual(s.canPartitionKSubsets(nums = [4,3,2,3,5,2,1], k = 4), True)
        self.assertEqual(s.canPartitionKSubsets(nums = [1,2,3,4], k = 3), False)
        


if __name__ == '__main__':
    unittest.main()