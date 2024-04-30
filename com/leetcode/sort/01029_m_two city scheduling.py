from typing import List
from typing import Deque
import heapq

class Solution:

    # Sort by diff of cost to A and cost to B
    # First n choose cost to A, second n choose cost to B
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        costs.sort(key=lambda cost: (cost[0] - cost[1]))
        return sum((costs[i][0] + costs[i + n][1]) for i in range(n))

import unittest

class TestSolution(unittest.TestCase):
    def testMiceAndCheese(self):
        s = Solution()
        self.assertEqual(s.miceAndCheese(reward1 = [1,1,3,4], reward2 = [4,4,1,1], k = 2), 15)
        self.assertEqual(s.miceAndCheese(reward1 = [1,1], reward2 = [1,1], k = 2), 2)
        self.assertEqual(s.miceAndCheese(reward1 = [3,5], reward2 = [3,5], k = 1), 8)
        self.assertEqual(s.miceAndCheese(reward1 = [1,4,4,6,4], reward2 = [6,5,3,6,1], k = 1), 24)
        self.assertEqual(s.miceAndCheese(reward1 = [1,2,1,2,1,2], reward2 = [2,1,1,2,2,1], k = 0), 9)


if __name__ == '__main__':
    unittest.main()