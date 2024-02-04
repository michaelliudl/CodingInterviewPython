from typing import List
from typing import Deque

class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        total = 1
        while self.stack and self.stack[-1][0] <= price:
            top = self.stack.pop()
            total += top[1]
        self.stack.append((price, total))
        return total


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

class Solution:

    pass

import unittest

class TestSolution(unittest.TestCase):
    def testMaxSlidingWindow(self):
        s = Solution()
        self.assertEqual(s.maxSlidingWindowMonoToneQueue1([1,3,-1,-3,5,3,6,7],3), [3,3,5,5,6,7])
        self.assertEqual(s.maxSlidingWindowMonoToneQueue1([1],1), [1])



if __name__ == '__main__':
    unittest.main()