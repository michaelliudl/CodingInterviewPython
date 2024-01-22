from typing import List

class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        
        

import unittest

class TestSolution(unittest.TestCase):
    def testMaxProfit(self):
        s = Solution()
        self.assertEqual(s.maxProfit(prices = [7,1,5,3,6,4]), 7)
        


if __name__ == '__main__':
    unittest.main()