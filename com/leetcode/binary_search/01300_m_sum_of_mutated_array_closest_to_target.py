from typing import List

class Solution:

    # Binary Search
    def findBestValue(self, arr: List[int], target: int) -> int:

        # Sum after replacing all value greater than midValue with midValue
        def getSum(midValue):
            result = 0
            for num in arr:
                result += num if num < midValue else midValue
            return result

        if not arr: return 0
        low,high = 0,max(arr)
        bestValue = -1

        while low <= high:
            mid = low + (high-low) // 2
            curSum = getSum(mid)
            if curSum <= target:
                bestValue = max(bestValue, mid)
                low = mid + 1
            else:
                high = mid - 1
        sumRoundDown = getSum(bestValue)
        sumRoundUp = getSum(bestValue + 1)
        if abs(sumRoundDown - target) <= abs(sumRoundUp - target):
            return bestValue
        else:
            return bestValue + 1

    # Sort, wrong on case `self.assertEqual(s.findBestValue(arr = [2,2], target = 3), 1)`
    def findBestValueSort(self, arr: List[int], target: int) -> int:
        if not arr: return 0
        arr.sort()
        prefix,n = 0,len(arr)
        for i in range(n):
            ans = round((target - prefix) / (n - i))
            if ans <= arr[i]:
                return ans
            prefix += arr[i]
        return arr[-1]
            

import unittest

class TestSolution(unittest.TestCase):
    def testFindBestValue(self):
        s = Solution()
        self.assertEqual(s.findBestValue(arr = [2,2], target = 3), 1)
        self.assertEqual(s.findBestValue(arr = [60864,25176,27249,21296,20204], target = 56803), 11361)
        self.assertEqual(s.findBestValue(arr = [4,9,3], target = 10), 3)
        self.assertEqual(s.findBestValue(arr = [2,3,5], target = 10), 5)


if __name__ == '__main__':
    unittest.main()