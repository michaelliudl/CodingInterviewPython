from typing import List

class Solution:

    # dp[i] = min cost to reach i
    # dp[i] = min((dp[i-1] + cost(i-1)), (dp[i-2] + cost(i-2)))
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        dp=[0,0]
        for i in range(2, len(cost)+1):
            newCost=min(dp[1]+cost[i-1], dp[0]+cost[i-2])
            dp[0]=dp[1]
            dp[1]=newCost
        return dp[-1]

import unittest

class TestSolution(unittest.TestCase):
    def testSubsets(self):
        s = Solution()
        self.assertEqual(s.subsets(nums = [1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        self.assertEqual(s.subsets(nums = [0]), [[],[0]])
        


if __name__ == '__main__':
    unittest.main()