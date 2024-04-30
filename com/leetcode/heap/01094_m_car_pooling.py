from typing import List
import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        if not trips:
            return True
        n = len(trips)
        tripSorted = [(fromTime, toTime, passengers) for passengers, fromTime, toTime in trips]
        tripSorted.sort()
        capRem = capacity
        heap = []
        for fromTime, toTime, passengers in tripSorted:
            while heap and heap[0][0] <= fromTime:
                top = heapq.heappop(heap)
                capRem += top[1]
            if capRem < passengers:
                return False
            heapq.heappush(heap, (toTime, passengers))
            capRem -= passengers
        return True


import unittest

class TestSolution(unittest.TestCase):
    def testCarPooling(self):
        s = Solution()
        self.assertEqual(s.carPooling(trips = [[9,3,4],[9,1,7],[4,2,4],[7,4,5]], capacity = 23), True)
        self.assertEqual(s.carPooling(trips = [[2,1,5],[3,3,7]], capacity = 5), True)
        self.assertEqual(s.carPooling(trips = [[2,1,5],[3,3,7]], capacity = 4), False)


if __name__ == '__main__':
    unittest.main()