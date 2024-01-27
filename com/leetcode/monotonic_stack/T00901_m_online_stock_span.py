from typing import List
from typing import Deque

class StockSpanner:

    def __init__(self):
        pass

    def next(self, price: int) -> int:
        pass


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