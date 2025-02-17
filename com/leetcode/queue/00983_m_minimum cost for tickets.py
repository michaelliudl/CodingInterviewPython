from typing import List, Deque
import math, functools

class Solution:

    # Use queues to find the minimum cost to cover each day
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        last7Days = Deque()
        last30Days = Deque()
        res = 0
        for day in days:
            while last7Days and last7Days[0][0] + 7 <= day:
                last7Days.popleft()
            while last30Days and last30Days[0][0] + 30 <= day:
                last30Days.popleft()
            last7Days.append((day, res + costs[1]))
            last30Days.append((day, res + costs[2]))
            res = min(res + costs[0], last7Days[0][1], last30Days[0][1])
        return res


import unittest

class TestSolution(unittest.TestCase):
    def testMinimumOperations(self):
        s = Solution()
        self.assertEqual(s.minimumOperations(grid = [[1,0,2],[1,0,2]]), 0)
        self.assertEqual(s.minimumOperations(grid = [[1,1,1],[0,0,0]]), 3)
        self.assertEqual(s.minimumOperations(grid = [[1],[2],[3]]), 2)


if __name__ == '__main__':
    unittest.main()