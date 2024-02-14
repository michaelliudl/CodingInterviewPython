from typing import List

class Solution:

    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        if not customers: return 0
        total, end = customers[0][1], customers[0][0] + customers[0][1]
        for i in range(1, len(customers)):
            arrival, time = customers[i]
            total += time if arrival >= end else (end - arrival + time)
            end += time if arrival < end else (arrival - end + time)
        return total / len(customers)

        

import unittest

class TestSolution(unittest.TestCase):

    def testAverageWaitingTime(self):
        s=Solution()
        self.assertEqual(s.averageWaitingTime(customers = [[1,2],[2,5],[4,3]]), 5.0)
        self.assertEqual(s.averageWaitingTime(customers = [[5,2],[5,4],[10,3],[20,1]]), 3.25)

if __name__ == '__main__':
    unittest.main()