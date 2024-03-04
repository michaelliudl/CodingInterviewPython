from typing import List

class Solution:

    # Prefix sum and use hash table to cache count of diffs
    # Similar to 325, 560, 1658
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums: return 0
        prefixSum, subArrayCount = 0, 0
        prefixSumToIndex = {0: 1}        # Track number of diff from prefixSum - k
        for _, num in enumerate(nums):
            prefixSum += num
            diff = prefixSum - k
            if diff in prefixSumToIndex:
                subArrayCount += prefixSumToIndex[diff]
            prefixSumToIndex[prefixSum] = prefixSumToIndex.get(prefixSum, 0) + 1
        return subArrayCount


import unittest

class TestSolution(unittest.TestCase):
    def testSubarraySum(self):
        s = Solution()
        self.assertEqual(s.subarraySum(nums = [1,-1,0], k = 0), 3)
        self.assertEqual(s.subarraySum(nums = [1,1,1], k = 2), 2)
        self.assertEqual(s.subarraySum(nums = [1,2,3], k = 3), 2)



if __name__ == '__main__':
    unittest.main()