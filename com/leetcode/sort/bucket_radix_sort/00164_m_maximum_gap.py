from typing import List,Optional
import heapq

class Solution:

    # Radix sort
    def maximumGap(self, nums: List[int]) -> int:

        def radixSort():
            maxVal = max(numsCopy)
            exponent = 1
            while maxVal // exponent > 0:
                count = [0] * 10
                temp = [0] * n
                for num in numsCopy:
                    countIndex = (num // exponent) % 10
                    count[countIndex] += 1
                for i in range(1,10):
                    count[i] += count[i-1]
                for num in reversed(numsCopy):
                    countIndex = (num // exponent) % 10
                    temp[count[countIndex] - 1] = num
                    count[countIndex] -= 1
                for i in range(n):
                    numsCopy[i] = temp[i]
                exponent *= 10

        if not nums or len(nums) < 2: return 0
        n = len(nums)
        numsCopy = nums[:]
        radixSort()
        ans = 0
        for i in range(n):
            ans = max(ans, (numsCopy[i] - numsCopy[i-1]))
        return ans

    # Same as sort
    def maximumGapSort(self, nums: List[int]) -> int:
        if not nums or len(nums) < 2: return 0
        heapq.heapify(nums)
        prev, maxGap = None, 0
        while nums:
            cur = heapq.heappop(nums)
            if prev:
                maxGap = max(maxGap, (cur - prev))
            prev = cur
        return maxGap

import unittest

class TestSolution(unittest.TestCase):
    def testMaximumGap(self):
        s = Solution()
        self.assertEqual(s.maximumGap(nums = [3,6,9,1]), 3)
        self.assertEqual(s.maximumGap(nums = [100,3,2,1]), 97)


if __name__ == '__main__':
    unittest.main()