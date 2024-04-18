from typing import List

class Solution:

    # Similar to 325, 560, 1658
    # Prefix sum and use hash table to cache remainder count of prefix sum % k
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        rems = {0:1}
        ret = 0
        for i, num in enumerate(nums):
            rem = num % k
            if rem in rems:
                ret += rems[rem]
            rems[rem] = rems.get(rem, 0) + 1
        return ret


import unittest

class TestSolution(unittest.TestCase):
    def testSubarraySum(self):
        s = Solution()
        self.assertEqual(s.subarraySum(nums = [1,-1,0], k = 0), 3)
        self.assertEqual(s.subarraySum(nums = [1,1,1], k = 2), 2)
        self.assertEqual(s.subarraySum(nums = [1,2,3], k = 3), 2)



if __name__ == '__main__':
    unittest.main()