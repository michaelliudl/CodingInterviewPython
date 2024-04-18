from typing import List

'''
Given an integer array nums which is sorted in ascending order and all of its elements are unique and given also an integer k, return the kth missing number starting from the leftmost number of the array.


'''
class Solution:

    def missingElement(self, nums: List[int], k: int) -> int:

        low, high = 0, len(nums)
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] - mid - nums[0] >= k:
                high = mid
            else:
                low = mid + 1
        # return nums[low - 1] + k - (nums[low - 1] - nums[0] - (low - 1))
        return nums[0] + k + low - 1

    # Binary search
    def missingElementBS1(self, nums: List[int], k: int) -> int:

        def missing(index):
            return nums[index] - nums[0] - index

        low, high = 0, len(nums)
        while low < high:
            mid = low + (high - low) // 2
            if missing(mid) >= k:
                high = mid
            else:
                low = mid + 1
        return nums[low - 1] + k - missing(low - 1)

    # Similar to 1539
    def missingElement1(self, nums: List[int], k: int) -> int:
        missing = nums[0] + 1
        for i in range(1, len(nums)):
            diff = nums[i] - missing
            if diff < k:
                k -= diff
                missing = nums[i] + 1
            else:
                return missing + k - 1
        return missing + k - 1

import unittest

class TestSolution(unittest.TestCase):
    def testMissingElement(self):
        s = Solution()
        self.assertEqual(s.missingElement(nums = [4,7,9,10], k = 1), 5)
        self.assertEqual(s.missingElement(nums = [4,7,9,10], k = 3), 8)
        self.assertEqual(s.missingElement(nums = [1,2,4], k = 3), 6)


if __name__ == '__main__':
    unittest.main()