from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not nums: return 0
        prod,left,ans = 1,0,0
        for i in range(len(nums)):
            prod *= nums[i]
            while left <= i and prod >= k:
                winOut = nums[left]
                prod //= winOut
                left += 1
            ans += (i-left+1)
        return ans




import unittest

class TestSolution(unittest.TestCase):
    def testNumSubarrayProductLessThanK(self):
        s = Solution()
        self.assertEqual(s.numSubarrayProductLessThanK(nums = [1,2,3], k = 0), 0)
        self.assertEqual(s.numSubarrayProductLessThanK(nums = [10,5,2,6], k = 100), 8)


if __name__ == '__main__':
    unittest.main()