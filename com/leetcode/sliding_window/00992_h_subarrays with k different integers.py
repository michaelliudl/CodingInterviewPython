from typing import List

class Solution:

    # # of subarrays with K distinct elements = (# of subarrays with at most K distinct elements) - (# of subarrays with at most K - 1 distinct elements)
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def subarraysWithAtMostKDistinct(k):
            distincts = {}
            result = left = 0
            for index, num in enumerate(nums):
                distincts[num] = distincts.get(num, 0) + 1
                while len(distincts) > k:
                    out = nums[left]
                    distincts[out] -= 1
                    if not distincts[out]:
                        del distincts[out]
                    left += 1
                result += (index - left + 1)
            return result

        if not nums or k <= 0:
            return 0
        return subarraysWithAtMostKDistinct(k) - subarraysWithAtMostKDistinct(k - 1)

import unittest

class TestSolution(unittest.TestCase):
    def testSubarraysWithKDistinct(self):
        s = Solution()
        self.assertEqual(s.subarraysWithKDistinct(nums = [1,2,1,2,3], k = 2), 7)
        self.assertEqual(s.subarraysWithKDistinct(nums = [1,2,1,3,4], k = 3), 3)


if __name__ == '__main__':
    unittest.main()