from typing import List,Deque

class Solution:

    # ??? TODO
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        if not arr or k<=0: return 0
        n=len(arr)
        dp = [0]* (n+1)
        for i in range(1, n+1):
            maxI = -float('inf')
            for j in range(1, min(k, i) + 1):
                maxI = max(maxI, arr[i-j])
                dp[i] = max(dp[i], dp[i-j] + maxI * j)
        return dp[n]



import unittest

class TestSolution(unittest.TestCase):
    def testMaxSumAfterPartitioning(self):
        s = Solution()
        self.assertEqual(s.maxSumAfterPartitioning(arr = [1,15,7,9,2,5,10], k = 3), 84)
        self.assertEqual(s.maxSumAfterPartitioning(arr = [1], k = 1), 1)
        self.assertEqual(s.maxSumAfterPartitioning(arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4), 83)


if __name__ == '__main__':
    unittest.main()