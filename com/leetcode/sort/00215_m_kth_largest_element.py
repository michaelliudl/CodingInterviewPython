from typing import List
import heapq
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) < k:
            return 0
        h=nums[:k]
        heapq.heapify(h)
        for n in nums[k:]:
            if n>h[0]:
                heapq.heappop(h)
                heapq.heappush(h,n)
        return h[0]
    
    # TODO Fix less than
    def findKthLargestQuickSelect(self, nums: List[int], k: int) -> int:

        def quickSelect(nums, low, high, target):
            if low < high:
                pivot_index = partition(nums, low, high)
                if pivot_index == target:
                    return nums[target]
                elif pivot_index < target:
                    return quickSelect(nums, low = pivot_index + 1, high = high, target = target)
                else:
                    return quickSelect(nums, low = low, high = pivot_index, target = target)
            return 0
        
        def partition(nums, low, high):
            pivot_index = random.randint(low, high)
            pivot = nums[pivot_index]
            nums[pivot_index], nums[high - 1] = nums[high - 1], nums[pivot_index]
            
            i=low
            for j in range(low, high):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i+=1
            nums[i], nums[high - 1] = nums[high - 1], nums[i]
            return i

        n=len(nums)
        return quickSelect(nums, low=0, high=n, target=(n-k))       # Quick select finds kth smallest
    
    # TODO Fix timeout
    def findKthLargestQuickSelect_1(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, 0, len(nums) - 1, (len(nums)-k))
    
    def quickSelect(self, nums: List[int], low: int, high: int, k: int) -> int:
        if low <= high:
            pivot_index = self.partition(nums, low, high)
            if pivot_index == k:
                return nums[pivot_index]
            elif pivot_index < k:
                return self.quickSelect(nums, pivot_index + 1, high, k)
            else:
                return self.quickSelect(nums, low, pivot_index - 1, k)
        return 0
    
    def partition(self, nums: List[int], low: int, high: int) -> int:
        pivot_index = random.randint(low, high)
        # pivot_index = int((low+high)/2)
        pivot = nums[pivot_index]
        nums[pivot_index], nums[high] = nums[high],nums[pivot_index]
        i = low

        for j in range(low,high):
            if nums[j]<=pivot:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
        nums[i],nums[high]=nums[high],nums[i]
        return i

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def testFindKthLargest(self):
        self.assertEqual(self.s.findKthLargestQuickSelect([3,2,1,5,6,4],2), 5)
        self.assertEqual(self.s.findKthLargestQuickSelect([3,2,3,1,2,4,5,5,6],4), 4)
        # self.s.partition([3,2,3,1,2,4,5,5,6], 0, 8)


if __name__ == '__main__':
    unittest.main()