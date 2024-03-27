from typing import List,Deque

class HitCounter:

    def __init__(self):
        self.queue = Deque()
        self.timeSpan = 300
        self.hits = 0

    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)
        self.hits += 1

    def getHits(self, timestamp: int) -> int:
        while self.queue and self.queue[0] <= timestamp - self.timeSpan:
            self.queue.popleft()
            self.hits -= 1
        return self.hits


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

class Solution:
    pass

import unittest

class TestSolution(unittest.TestCase):
    def testHitCounter(self):
        hc = HitCounter()
        hc.hit(1)
        hc.hit(2)
        hc.hit(3)
        self.assertEqual(hc.getHits(4), 3)
        hc.hit(300)
        self.assertEqual(hc.getHits(300), 4)
        self.assertEqual(hc.getHits(301), 3)


if __name__ == '__main__':
    unittest.main()