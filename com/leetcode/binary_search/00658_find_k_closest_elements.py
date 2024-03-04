from typing import List

class Solution:

    # Binary search to find start index of the k elements
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if not arr:
            return []
        low, high = 0, len(arr) - k
        while low < high:
            mid = low + (high - low) // 2
            if x - arr[mid] <= arr[mid + k] - x:
                high = mid
            else:
                low = mid + 1
        return arr[low : low + k]

    # O(n) using sliding window or heap
    def findClosestElements1(self, arr: List[int], k: int, x: int) -> List[int]:
        if not arr:
            return []
        minDiff, minDiffIndex = float('inf'), -1
        for index, num in enumerate(arr):
            diff = abs(num - x)
            if diff < minDiff:
                minDiff = diff
                minDiffIndex = index
        left = right = minDiffIndex
        while right - left + 1 < k:
            leftDiff = abs(arr[left - 1] - x) if left - 1 >=0 else float('inf')
            rightDiff = abs(arr[right + 1] - x) if right + 1 < len(arr) else float('inf')
            if leftDiff <= rightDiff:
                left -= 1
            elif right - left + 1 < k and right + 1 < len(arr):
                right += 1
        return arr[left : right + 1]

import unittest

class TestSolution(unittest.TestCase):
    def testFindClosestElements(self):
        s = Solution()
        self.assertEqual(s.findClosestElements(arr = [0,1,1,1,2,3,6,7,8,9], k = 9, x = 4), [0,1,1,1,2,3,6,7,8])
        self.assertEqual(s.findClosestElements(arr = [1,2,3,4,5], k = 4, x = 3), [1,2,3,4])
        self.assertEqual(s.findClosestElements(arr = [1,2,3,4,5], k = 4, x = -1), [1,2,3,4])


if __name__ == '__main__':
    unittest.main()