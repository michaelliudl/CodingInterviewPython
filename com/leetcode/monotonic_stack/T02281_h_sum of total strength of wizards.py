from typing import List
import itertools

class Solution:

    # Same as 1856, change max to sum
    # 1 pass to get product of min value and subarray sub
    def totalStrength(self, strength: List[int]) -> int:
        if not strength:
            return 0
        nums = [0] + strength + [0]
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        res = 0
        stack = []
        for i in range(n):
            while stack and nums[i] < nums[stack[-1]]:
                minVal = nums[stack.pop()]
                subSum = prefix[i] - prefix[stack[-1] + 1]
                res += minVal * subSum
                res %= (10 ** 9 + 7)
            stack.append(i)
        return res
    

import unittest

class TestSolution(unittest.TestCase):
    def testTotalStrength(self):
        s = Solution()
        self.assertEqual(s.totalStrength(strength = [1,3,1,2]), 44)
        self.assertEqual(s.totalStrength(strength = [5,4,6]), 213)
        


if __name__ == '__main__':
    unittest.main()