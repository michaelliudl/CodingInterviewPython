from typing import List

class Solution:

    # Modified binary search
    def singleNonDuplicate1(self, nums: List[int]) -> int:
        if not nums:
            return - 1
        if len(nums) < 3:
            return nums[0]
        n = len(nums)
        low, high = 0, n
        while low < high:
            mid = low + (high - low) // 2
            # Result value doesn't equal to neighbors before and after
            if (mid == 0 and nums[mid] != nums[mid + 1]) \
                or (mid == n - 1 and nums[mid - 1] != nums[mid]) \
                    or (nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]):
                return nums[mid]
            # Move low/high based on: before single element, pair's first index is odd, second is even;
            # After single element, pair's first index is even, second is odd
            if mid > 0 and nums[mid] == nums[mid - 1]:
                if mid % 2 == 0:
                    high = mid
                else:
                    low = mid + 1
            elif mid < n - 1 and nums[mid] == nums[mid + 1]:
                if mid % 2 == 1:
                    high = mid
                else:
                    low = mid + 1
        return -1

    # Modified binary search
    def singleNonDuplicate1(self, nums: List[int]) -> int:
        if not nums: return -1
        if len(nums)<3: return nums[0]
        n = len(nums)
        low,high = 0,n-1
        while low<high:
            mid = low + (high-low)//2
            if mid%2 == 1:
                mid -= 1        # Update `mid` to even number
            if nums[mid] != nums[mid+1]:
                high = mid
            else:
                low = mid + 2
        return nums[low]


    # O(n)
    def singleNonDuplicateON(self, nums: List[int]) -> int:

        def search(low,high):
            mid = low + (high-low) // 2
            if mid == 0:
                return nums[mid] if nums[mid] != nums[mid+1] else -1
            if mid == n-1:
                return nums[mid] if nums[mid] != nums[mid-1] else -1
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            if low == high:
                return -1
            result = search(low,mid)
            if result == -1:
                result = search(mid+1,high)
            return result


        if not nums: return -1
        if len(nums)<3: return nums[0]
        n = len(nums)
        return search(0,n)
            

import unittest

class TestSolution(unittest.TestCase):
    def testSingleNonDuplicate(self):
        s = Solution()
        self.assertEqual(s.singleNonDuplicate(nums = [3,3,7,7,10,11,11]), 10)
        self.assertEqual(s.singleNonDuplicate(nums = [1,1,2,3,3,4,4,8,8]), 2)


if __name__ == '__main__':
    unittest.main()