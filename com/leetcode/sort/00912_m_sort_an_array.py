from typing import List
import heapq
import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def partition(low, high):
            randIndex = random.randint(low, high)
            pivot = nums[randIndex]
            nums[randIndex], nums[high] = nums[high], nums[randIndex]
            left = low
            for i in range(low, high):
                if nums[i] <= pivot:
                    nums[left], nums[i] = nums[i], nums[left]
                    left += 1
            nums[left], nums[high] = nums[high], nums[left]
            return left

        def quickSort(low, high):
            if low >= high:
                return
            pivotIndex = partition(low, high)
            quickSort(low, pivotIndex - 1)
            quickSort(pivotIndex + 1, high)
        
        def merge(low, mid, high):
            temp = [-float('inf')] * (high - low + 1)
            pLow, pHigh, pT = low, mid + 1, 0
            while pLow <= mid and pHigh <= high:
                if nums[pLow] <= nums[pHigh]:
                    temp[pT] = nums[pLow]
                    pLow += 1
                else:
                    temp[pT] = nums[pHigh]
                    pHigh += 1
                pT += 1
            while pLow <= mid:
                temp[pT] = nums[pLow]
                pLow += 1
                pT += 1
            while pHigh <= high:
                temp[pT] = nums[pHigh]
                pHigh += 1
                pT += 1
            for i in range(low, high + 1):
                nums[i] = temp[i - low]

        def mergeSort(low, high):
            if high - low <= 11:
                quickSort(low, high)
                return
            mid = low + (high - low) // 2
            mergeSort(low, mid)
            mergeSort(mid + 1, high)
            merge(low, mid, high)

        if not nums or len(nums) <= 1:
            return nums
        # Both Merge sort and Quick sort use inclusive boundaries
        mergeSort(low = 0, high = len(nums) - 1)
        return nums

import unittest

class TestSolution(unittest.TestCase):
    def testSortArray(self):
        s = Solution()
        self.assertEqual(s.sortArray(nums = [5,2,3,1]), [1,2,3,5])
        self.assertEqual(s.sortArray(nums = [5,1,1,2,0,0]), [0,0,1,1,2,5])


if __name__ == '__main__':
    unittest.main()