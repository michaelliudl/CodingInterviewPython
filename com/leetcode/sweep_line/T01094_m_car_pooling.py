from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        if not trips:
            return True
        n = len(trips)
        tripSorted = [None] * n
        for i, [passengers, fromTime, toTime] in enumerate(trips):
            tripSorted[i] = (fromTime, toTime, passengers)
        tripSorted.sort()
        capTaken = end = 0
        for fromTime, toTime, passengers in tripSorted:
            if end == 0:
                end = toTime
                capTaken = passengers
                continue
            elif fromTime < end:
                capTaken += passengers
            else:
                capTaken = passengers
            if capTaken > capacity:
                return False
            if end < toTime:
                end = toTime
                capTaken = passengers
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