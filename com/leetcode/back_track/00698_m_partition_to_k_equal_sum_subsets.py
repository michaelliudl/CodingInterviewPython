from typing import List

class Solution:

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        def backtrack(start):
            if start==n:                    # At the end, should have all sums with same value
                for subset in subsets:
                    if subset!=subSum:
                        return False
                return True
            for i in range(k):
                if subsets[i]+nums[start]<=subSum:  # For each subset value, sum and backtrack with all start positions to reach subSum
                    subsets[i]+=nums[start]
                    found=backtrack(start+1)
                    if found: return True
                    subsets[i]-=nums[start]
                
                if subsets[i]==0:
                    break
            return False

        if not nums or len(nums)<k: return False
        total=sum(nums)
        if total%k!=0: return False

        subSum=total//k
        n=len(nums)
        nums.sort(reverse=True)
        subsets=[0]*k               # Calculate k sums
        r=backtrack(start=0)
        return r

import unittest

class TestSolution(unittest.TestCase):
    def testCanPartitionKSubsets(self):
        s = Solution()
        self.assertEqual(s.canPartitionKSubsets(nums = [4,3,2,3,5,2,1], k = 4), True)
        self.assertEqual(s.canPartitionKSubsets(nums = [1,1,1,1,2,2,2,2], k = 4), True)
        self.assertEqual(s.canPartitionKSubsets(nums = [1,1,1,1,2,2,2,2], k = 2), True)
        self.assertEqual(s.canPartitionKSubsets(nums = [1,2,3,4], k = 3), False)
        


if __name__ == '__main__':
    unittest.main()