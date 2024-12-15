from typing import Optional,List,Deque
import math

class Solution:

    def canSortArray(self, nums: List[int]) -> bool:
        # Divide the array into segments that each segment contains consecutive elements sharing an equal number of set bits.
        # Ensure that max of prev segment is less than min of next segment
        prevSetBits = 0
        prevMax = -math.inf
        curMax = -math.inf
        curMin = math.inf

        for num in nums:
            setBits = num.bit_count()
            if setBits != prevSetBits:
                if prevMax > curMin:
                    return False
                prevSetBits = setBits
                prevMax = curMax
                curMax = num
                curMin = num
            else:
                curMax = max(curMax, num)
                curMin = min(curMin, num)
        return prevMax <= curMin

import unittest

class TestSolution(unittest.TestCase):
    def testSortByBits(self):
        s = Solution()
        self.assertEqual(s.sortByBits(arr = [0,1,2,3,4,5,6,7,8]), [0,1,2,4,8,3,5,6,7])
        self.assertEqual(s.sortByBits(arr = [1024,512,256,128,64,32,16,8,4,2,1]), [1,2,4,8,16,32,64,128,256,512,1024])

if __name__ == '__main__':
    unittest.main()