from typing import List
import math

class Solution:

    # Use 32 lenght integer array to track # of `1` bits in the window
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:

        def setBits(num, add):
            index = 0
            while num > 0:
                if num & 1 == 1:
                    oneBits[index] += 1 if add else -1
                num >>= 1
                index += 1
        
        def convertBits():
            result = 0
            for i in range(32):
                if oneBits[i] > 0:
                    result |= (1 << i)
            return result

        if not nums or k < 0:
            return 0
        oneBits = [0] * 32
        left = 0
        result = math.inf
        orResult = 0
        for i in range(len(nums)):
            setBits(nums[i], add=True)
            orResult = convertBits()
            while left <= i and orResult >= k:
                result = min(result, (i - left + 1))
                setBits(nums[left], add=False)
                orResult = convertBits()
                left += 1
        return result


import unittest

class TestSolution(unittest.TestCase):
    def testMinimumSubarrayLength(self):
        s = Solution()
        self.assertEqual(s.minimumSubarrayLength(nums = [1,2], k = 0), 1)
        self.assertEqual(s.minimumSubarrayLength(nums = [1,2,3], k = 2), 1)
        self.assertEqual(s.minimumSubarrayLength(nums = [2,1,8], k = 10), 3)
        self.assertEqual(s.minimumSubarrayLength(nums = [16,1,2,20,32], k = 45), 2)


if __name__ == '__main__':
    unittest.main()