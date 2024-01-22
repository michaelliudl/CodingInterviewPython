from typing import List

class Solution:


    def rob(self, nums: List[int]) -> int:

        def dpRob(start, end):
            dp=[0]*(end-start)
            dp[0]=nums[start]
            dp[1]=max(nums[start],nums[start+1])
            for i in range(2, end-start):
                dp[i]=max(dp[i-1], dp[i-2]+nums[start+i])
            return dp[-1]

        if not nums:
            return 0
        if len(nums)<=2:
            return max(nums)
        # Calcualate 2 subarrays one without head, one without tail
        m1=dpRob(0, len(nums)-1)
        m2=dpRob(1, len(nums))
        return max(m1,m2)



import unittest

class TestSolution(unittest.TestCase):
    def testSubsets(self):
        s = Solution()
        self.assertEqual(s.subsets(nums = [1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        self.assertEqual(s.subsets(nums = [0]), [[],[0]])
        


if __name__ == '__main__':
    unittest.main()