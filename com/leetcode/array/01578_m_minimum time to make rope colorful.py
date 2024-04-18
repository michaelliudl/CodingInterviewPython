from typing import List

class Solution:

    # Maintain sum and max time for each color and subtract
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        if not colors or not neededTime or len(colors) != len(neededTime):
            return 0
        n = len(colors)
        color = colors[0]
        curMax = neededTime[0]
        curSum = neededTime[0]
        result = 0
        for i in range(1, n):
            if colors[i] == color:
                curMax = max(curMax, neededTime[i])
                curSum += neededTime[i]
            else:
                result += (curSum - curMax)
                color = colors[i]
                curMax = curSum = neededTime[i]
        result += (curSum - curMax)
        return result


        

import unittest

class TestSolution(unittest.TestCase):

    def testSortedSquares(self):
        s = Solution()
        self.assertEqual(s.minCost(colors = "aaabbbabbbb", neededTime = [3,5,10,7,5,3,5,5,4,8,1]), 26)
        self.assertEqual(s.minCost(colors = "abaac", neededTime = [1,2,3,4,5]), 3)
        self.assertEqual(s.minCost(colors = "abc", neededTime = [1,2,3]), 0)
        self.assertEqual(s.minCost(colors = "aabaa", neededTime = [1,2,3,4,1]), 2)

if __name__ == '__main__':
    unittest.main()