from typing import List
from typing import Deque


class Solution:

    # Monotonic stack for index to update values
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                prices[stack.pop()] -= price
            stack.append(i)
        return prices

    # Brute force
    def finalPricesBrute(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break
        return prices

import unittest

class TestSolution(unittest.TestCase):
    def testMaxSlidingWindow(self):
        s = Solution()
        self.assertEqual(s.maxSlidingWindowMonoToneQueue1([1,3,-1,-3,5,3,6,7],3), [3,3,5,5,6,7])
        self.assertEqual(s.maxSlidingWindowMonoToneQueue1([1],1), [1])



if __name__ == '__main__':
    unittest.main()