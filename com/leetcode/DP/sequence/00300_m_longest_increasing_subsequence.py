from typing import List

class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        active=[0]*len(nums)
        size=0

        for num in nums:
            left,right=0,size

            while left<right:
                mid=left+(right-left)//2
                if active[mid]<num:
                    left=mid+1
                else:
                    right=mid
            
            active[left]=num
            if left==size:
                size+=1
        return size

    # dp[i] is LIS at i inclusive. It's calculate by looping j = [0,i-1].
    # dp[i] = max(dp[i], dp[j]+1) if nums[j]>nums[i], j = [0,i-1]
    def lengthOfLISDP(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp=[1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i], dp[j]+1)
        return max(dp)



import unittest

class TestSolution(unittest.TestCase):
    def testLengthOfLIS(self):
        s = Solution()
        self.assertEqual(s.lengthOfLIS(nums = [10,9,2,5,3,7,101,18]), 4)
        self.assertEqual(s.lengthOfLIS(nums = [0,1,0,3,2,3]), 4)
        self.assertEqual(s.lengthOfLIS(nums = [7,7,7,7,7,7,7]), 1)
        


if __name__ == '__main__':
    unittest.main()