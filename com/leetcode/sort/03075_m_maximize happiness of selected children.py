from typing import List
from typing import Deque
import heapq

class Solution:

    # Sort in reverse order and simulate
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        res = 0
        for i in range(len(happiness)):
            if i == k:
                break
            res += ((happiness[i] - i) if (happiness[i] - i) >= 0 else 0)
        return res

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