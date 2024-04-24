from typing import List
import itertools

class Solution:

    # Similar to 1856, finding max product of min value and subarray sum, which can use prefix sum directly
    # This one needs to sum up all products of min value and respective subarray sums.
    # Hard part is to get all subarray sums that have each value as min. Some elements in the subarrays need to be used multiple times.
    # Below uses prefix sum that accumulates twice
    def totalStrength(self, strength: List[int]) -> int:
        if not strength:
            return 0
        nums = strength
        n = len(nums)
        prefix = [0] * (n + 1)      # Accumulate prefix sum twice!!
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        for i in range(n):
            prefix[i + 1] += prefix[i]

        nextSmaller = [n] * n
        prevSmallerOrEqual = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[i] < nums[stack[-1]]:
                nextSmaller[stack.pop()] = i
            if stack:
                prevSmallerOrEqual[i] = stack[-1]
            stack.append(i)

        res = 0
        for i in range(n):
            prev = prevSmallerOrEqual[i]
            next = nextSmaller[i]
            prevSubLen = i - prev
            nextSubLen = next - i
            prevSubSum = prefix[i] - prefix[max(0, prev)]
            nextSubSum = prefix[next] - prefix[i]
            res += nums[i] * (nextSubSum * prevSubLen - prevSubSum * nextSubLen)    # This gives sum of all subarrays with nums[i] as min value
            res %= (10 ** 9 + 7)
        return res

    # Below uses prefix sum with index as weight
    # x = i - a, y = b = i      Number of subarrays on left and right of `i`
    # a X X X X i X X X b       `i` is current index and min value of subarrays marked as `X` which are greater than nums[i], nums[a] and nums[b] are smaller than nums[i]
    #   1 2 3 4   3 2 1         Look at different subarrays, these numbers are how many times each `X` should be included in subarray sums on respective side of `i`
    # All elements on left of `i` should be counted `y` times, and all elements on right of `i` should be counted `x` times.
    # subSum[i] = (nums[a+1]*1, nums[a+2]*2, nums[a+3]*3, nums[a+4]*4) * y)
    #           + (nums[i+1]*3, nums[i+2]*2, nums[i+3]*1) * x)
    #           + (nums[i] * x * y)
    # leftSubSum[i] = (nums[a+1]*1, nums[a+2]*2, nums[a+3]*3, nums[a+4]*4) = (nums[i-4]*1, nums[i-3]*2, nums[i-2]*3, nums[i-1]*4)
    # rightSubSum[i] = (nums[i+1]*3, nums[i+2]*2, nums[i+3]*1) = (nums[b-3]*3, nums[b-2]*2, nums[b-1]*1)
    # prefixSumWithIndex[i] = nums[1]*1 + nums[2]*2 + ... + nums[i]*i
    # prefixSumWithIndex[i-1] - prefixSumWithIndex[a] = (nums[a+1]*(a+1), nums[a+2]*(a+2), nums[a+3]*(a+3), nums[a+4]*(a+4))
    #       = leftSubSum[i] + (prefixSum[i-1] - prefixSum[a]) * a
    # prefixSumWithIndex[b-1] - prefixSumWithIndex[i] = (nums[i+1]*(i+1), nums[i+2]*(i+2), nums[i+3]*(i+3), nums[i+4]*(i+4))
    #       = (prefixSum[b-1] - prefixSum[i]) * b - rightSubSum[i]
    def totalStrength1(self, strength: List[int]) -> int:
        if not strength:
            return 0
        nums = [0] + strength
        n = len(nums)
        prefixSum = [0] * (n + 1)
        for i in range(1, n):
            prefixSum[i] = prefixSum[i - 1] + nums[i]
        prefixSumWithIndex = [0] * (n + 1)
        for i in range(1, n):
            prefixSumWithIndex[i] = prefixSumWithIndex[i - 1] + nums[i] * i

        nextSmaller = [n] * n
        prevSmallerOrEqual = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[i] < nums[stack[-1]]:
                nextSmaller[stack.pop()] = i
            if stack:
                prevSmallerOrEqual[i] = stack[-1]
            stack.append(i)

        res = 0
        for i in range(n):
            prev = prevSmallerOrEqual[i]
            next = nextSmaller[i]
            prevSubLen = i - prev
            nextSubLen = next - i
            prevSubSum = (prefixSumWithIndex[i - 1] - prefixSumWithIndex[max(0, prev)]) - (prefixSum[i - 1] - prefixSum[max(0, prev)]) * max(0, prev)
            nextSubSum = (prefixSum[next - 1] - prefixSum[i]) * next - (prefixSumWithIndex[next - 1] - prefixSumWithIndex[i])
            res += nums[i] * (prevSubSum * nextSubLen + nextSubSum * prevSubLen + nums[i] * prevSubLen * nextSubLen)    # This gives sum of all subarrays with nums[i] as min value
            res %= (10 ** 9 + 7)
        return res
    

import unittest

class TestSolution(unittest.TestCase):
    def testTotalStrength(self):
        s = Solution()
        self.assertEqual(s.totalStrength(strength = [1,3,1,2]), 44)
        self.assertEqual(s.totalStrength(strength = [5,4,6]), 213)
        


if __name__ == '__main__':
    unittest.main()