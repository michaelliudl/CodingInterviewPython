from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        pass

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        pass


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

class Solution:

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
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