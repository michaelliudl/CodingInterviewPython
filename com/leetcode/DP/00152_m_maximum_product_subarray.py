from typing import List

class Solution:

    # dp_min[i] is min product for subarray up to i. It could be a bigger product if it's negative and later multiplied by another negative
    # dp_max[i] is max product for subarray up to i
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        ans, dpMin, dpMax = nums[0], nums[0], nums[0]
        for i in range(1,len(nums)):
            cur = nums[i]
            if cur < 0:
                prevMin = dpMin
                dpMin = min(cur, dpMax * cur)
                dpMax = max(cur, prevMin * cur)
            else:
                dpMin = min(cur, dpMin * cur)
                dpMax = max(cur, dpMax * cur)
            ans = max(ans, dpMax)
        return ans

    # Split by 0
    # If odd number of negatives, calculate product after first negative and before last negative
    def maxProduct1(self, nums: List[int]) -> int:

        def maxProduct(low, high):
            if low>=high: return nums[low] if low<n else 0
            negatives = [i for i in range(low, high+1) if nums[i]<0]
            ans=1
            if len(negatives)%2 == 0:
                for i in range(low, high+1):
                    ans *= nums[i]
                return ans
            for i in range(low, negatives[-1]):
                ans *= nums[i]
            prod=1
            for i in range(negatives[0]+1, high+1):
                prod *= nums[i]
            return max(ans, prod)


        if not nums: return 0
        n=len(nums)
        zeroes = [i for i in range(n) if nums[i] == 0]
        ans=0
        if zeroes:
            start = 0
            for i in range(len(zeroes)):
                ans = max(ans, maxProduct(low=start, high=zeroes[i]-1))
                start = zeroes[i] + 1
            ans = max(ans, maxProduct(start, n-1))
        else:
            ans = maxProduct(low=0, high=n-1)
        return ans
        

        

import unittest

class TestSolution(unittest.TestCase):

    def testMaxProduct(self):
        s=Solution()
        self.assertEqual(s.maxProduct(nums = [0]), 0)
        self.assertEqual(s.maxProduct(nums = [0,2]), 2)
        self.assertEqual(s.maxProduct(nums = [2,3,-2,4]), 6)
        self.assertEqual(s.maxProduct(nums = [-2,0,-1]), 0)

if __name__ == '__main__':
    unittest.main()