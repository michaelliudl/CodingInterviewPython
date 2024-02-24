from typing import List
import random
class Solution:
    def __init__(self, w: List[int]):
        # Use prefix sum to accumulate weights
        self.prefixSum = [w[0]]
        for i in range(1, len(w)):
            self.prefixSum.append(w[i] + self.prefixSum[i-1])
        
        ####
        # Brutaly expanding array per weight. Doesn't work on large input.
        # self.arr = []
        # for i in range(len(w)):
        #     for _ in range(w[i]):
        #         self.arr.append(i)

    def pickIndex(self) -> int:
        totalWeight = self.prefixSum[-1]
        # Random weight value. Use binary search to find index of this random weight in prefix sum
        randWeight = random.randint(1, totalWeight)
        left,right = 0, len(self.prefixSum)
        while left < right:
            mid = left + (right - left) // 2
            midWeight = self.prefixSum[mid]
            if midWeight == randWeight:
                return mid
            elif midWeight > randWeight:
                right = mid
            else:
                left = mid + 1
        return left

        ####
        # Brute search
        # r = random.randint(0, len(self.arr)-1)
        # return self.arr[r]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
            

import unittest

class TestSolution(unittest.TestCase):
    def testPickIndex(self):
        s = Solution([3,14,1,7])
        self.assertEqual(s.pickIndex(), 1)


if __name__ == '__main__':
    unittest.main()