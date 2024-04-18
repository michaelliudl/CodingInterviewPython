from typing import List

class Solution:

    # Solution 2, similar to 930 after converting odd number to 1 and even to 0
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        nums = [1 if num & 1 else 0 for num in nums]
        preSumCount = {0:1}
        ret = 0
        preSum = 0
        for num in nums:
            preSum += num
            diff = preSum - k
            if diff in preSumCount:
                ret += preSumCount[diff]
            preSumCount[preSum] = preSumCount.get(preSum, 0) + 1
        return ret

    # Solution 1, similar to 992
    # Number of subarrays with K odds = (# of subarrays with at most K odds) - (# of subarrays with at most K - 1 odds)
    def numberOfSubarraysAtMost(self, nums: List[int], k: int) -> int:

        def numberOfSubarraysWithAtMostKOddNumber(myK):
            ret = 0
            odds = 0
            left = 0
            for i, num in enumerate(nums):
                odds += 1 if num & 1 else 0
                while odds > myK:
                    odds -= 1 if nums[left] & 1 else 0
                    left += 1
                ret += (i - left + 1)
            return ret

        if not nums:
            return 0
        return numberOfSubarraysWithAtMostKOddNumber(myK = k) - numberOfSubarraysWithAtMostKOddNumber(myK = k - 1)



import unittest

class TestSolution(unittest.TestCase):
    def testSubarraysWithKDistinct(self):
        s = Solution()
        self.assertEqual(s.subarraysWithKDistinct(nums = [1,2,1,2,3], k = 2), 7)
        self.assertEqual(s.subarraysWithKDistinct(nums = [1,2,1,3,4], k = 3), 3)


if __name__ == '__main__':
    unittest.main()