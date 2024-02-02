from typing import List
import heapq

class MedianFinder:

    # Use order flag to reduce sort. Almost timeout
    def __init__(self):
        self.heapLeft, self.heapRight = [], []

    def addNum(self, num: int) -> None:
        if len(self.heapLeft) <= len(self.heapRight):
            if not self.heapRight or num <= self.heapRight[0]:
                heapq.heappush(self.heapLeft, -num)
            else:
                heapq.heappush(self.heapRight, num)
                heapq.heappush(self.heapLeft, -heapq.heappop(self.heapRight))
        else:
            if num >= -self.heapLeft[0]:
                heapq.heappush(self.heapRight, num)
            else:
                heapq.heappush(self.heapLeft, -num)
                heapq.heappush(self.heapRight, -heapq.heappop(self.heapLeft))

    def findMedian(self) -> float:
        if len(self.heapLeft) > len(self.heapRight):
            return float(-self.heapLeft[0])
        else:
            return (self.heapRight[0] - self.heapLeft[0]) / 2

class MedianFinder_1:

    # Use order flag to reduce sort. Almost timeout
    def __init__(self):
        self.data = []
        self.length = 0
        self.order = True

    def addNum(self, num: int) -> None:
        self.data.append(num)
        self.length += 1
        self.order = False

    def findMedian(self) -> float:
        if not self.order:
            self.data.sort()
            self.order = True
        if self.length % 2 == 1:
            return float(self.data[self.length // 2])
        else:
            return (self.data[self.length // 2] + self.data[self.length // 2 - 1]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

class Solution:
    pass


import unittest

class TestSolution(unittest.TestCase):
    def testMinAddToMakeValid(self):
        s = Solution()
        self.assertEqual(s.minAddToMakeValid("())"), 1)
        self.assertEqual(s.minAddToMakeValid("((("), 3)


if __name__ == '__main__':
    unittest.main()