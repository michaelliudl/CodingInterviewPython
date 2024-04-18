from typing import List

class Solution:

    # Standard prefix sum
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if not arr:
            return 0
        n = len(arr)
        for i in range(1, n):
            arr[i] += arr[i - 1]
        ret = 0
        print(arr)
        for i in range(k - 1, n):
            if arr[i]  - (arr[i - k] if i - k >= 0 else 0) >= threshold * k:
                ret += 1
        return ret

import unittest

class TestSolution(unittest.TestCase):
    def testMaxSumTwoNoOverlap(self):
        s = Solution()
        self.assertEqual(s.maxSumTwoNoOverlap(nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2), 20)
        self.assertEqual(s.maxSumTwoNoOverlap(nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2), 29)
        self.assertEqual(s.maxSumTwoNoOverlap(nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen = 3), 31)
        


if __name__ == '__main__':
    unittest.main()