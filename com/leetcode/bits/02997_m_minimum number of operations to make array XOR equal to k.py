from typing import Optional,List,Deque


class Solution:

    # XOR all in `nums` then sum diff bits with k
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = nums[0]
        for i in range(1, len(nums)):
            xor ^= nums[i]
        res = 0
        while xor > 0 or k > 0:
            res += 0 if ((xor & 1 and k & 1) or (not (xor & 1) and not (k & 1))) else 1
            xor >>= 1
            k >>= 1
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testSortByBits(self):
        s = Solution()
        self.assertEqual(s.sortByBits(arr = [0,1,2,3,4,5,6,7,8]), [0,1,2,4,8,3,5,6,7])
        self.assertEqual(s.sortByBits(arr = [1024,512,256,128,64,32,16,8,4,2,1]), [1,2,4,8,16,32,64,128,256,512,1024])

if __name__ == '__main__':
    unittest.main()