from typing import List

class Solution:

    # Fixed length window sum, try prefix sum
    # Find min sum of subarray length of n - k
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if not cardPoints or k == 0:
            return 0
        n = len(cardPoints)
        if k >= n:
            return sum(cardPoints)
        prefixSum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefixSum[i] = prefixSum[i - 1] + cardPoints[i - 1]
        minPrefixSum = float('inf')
        for i in range(n - k, n + 1):
            minPrefixSum = min(minPrefixSum, prefixSum[i] - prefixSum[i - (n - k)])
        return prefixSum[-1] - minPrefixSum

import unittest

class TestSolution(unittest.TestCase):
    def testFindItinerary(self):
        s = Solution()
        # self.assertEqual(s.findItinerary(tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]), 
        #                  ["JFK","MUC","LHR","SFO","SJC"])
        # self.assertEqual(s.findItinerary(tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]),
        #                  ["JFK","ATL","JFK","SFO","ATL","SFO"])
        # self.assertEqual(s.findItinerary(tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]),
        #                  ["JFK","NRT","JFK","KUL"])
        self.assertEqual(s.findItinerary(tickets = [['AAA', 'BBB'], ['ATL', 'AAA'], ['BBB', 'ATL'], ['JFK', 'ATL'], ['JFK', 'SFO'], ['SFO', 'JFK']]),
                         ['JFK', 'SFO', 'JFK', 'ATL', 'AAA', 'BBB', 'ATL'])
        self.assertEqual(s.findItinerary(tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","JFK"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"]]),
                         ["JFK","SFO","JFK","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL"])
        


if __name__ == '__main__':
    unittest.main()