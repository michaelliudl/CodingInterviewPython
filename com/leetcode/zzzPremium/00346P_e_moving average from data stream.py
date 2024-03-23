from typing import Deque

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = Deque()
        self.total = 0

    def next(self, val: int) -> float:
        if len(self.queue) == self.size:
            out = self.queue.popleft()
            self.total -= out
        self.queue.append(val)
        self.total += val
        return self.total / (self.size if len(self.queue) == self.size else len(self.queue))


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

class Solution:
    pass
    
import unittest

class TestSolution(unittest.TestCase):
    def testMovingAverage(self):
        ma = MovingAverage(3)
        self.assertEqual(ma.next(1), 1.0)
        self.assertEqual(ma.next(10), 5.5)
        self.assertEqual(ma.next(3), 4.666666666666667)
        self.assertEqual(ma.next(5), 6.0)
    


if __name__ == '__main__':
    unittest.main()
