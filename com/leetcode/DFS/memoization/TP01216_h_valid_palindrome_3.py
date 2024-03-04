from typing import List

class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        pass

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