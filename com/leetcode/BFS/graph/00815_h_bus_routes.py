from typing import List,Deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        def buildGraph():
            for i in range(len(routes)):
                bus,stops = i,routes[i]
                if bus not in busToStops:
                    busToStops[bus] = []
                for j in range(len(stops)):
                    stop = stops[j]
                    if stop not in stopToBuses:
                        stopToBuses[stop] = []
                    busToStops[bus].append(stop)
                    stopToBuses[stop].append(bus)

        if not routes: return -1
        busToStops = {}
        stopToBuses = {}
        buildGraph()
        ans,usedBuses,queue = 0,set(),Deque()
        queue.append(source)
        while queue:
            curLen = len(queue)
            for _ in range(curLen):
                stop = queue.popleft()
                if stop == target:
                    return ans
                if stop in stopToBuses:
                    buses = stopToBuses[stop]
                    for bus in buses:
                        if bus not in usedBuses:
                            usedBuses.add(bus)
                            for otherStop in busToStops[bus]:
                                if otherStop != stop:
                                    queue.append(otherStop)
            ans += 1
        return -1



        

import unittest

class TestSolution(unittest.TestCase):
    def testNumBusesToDestination(self):
        s = Solution()
        self.assertEqual(s.numBusesToDestination(routes = [[1,2,7],[3,6,7]], source = 1, target = 6), 2)
        self.assertEqual(s.numBusesToDestination(routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12), -1)
        


if __name__ == '__main__':
    unittest.main()