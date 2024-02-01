from typing import List

class Solution:


    # Memory limit exceed when endtime is 10**9
    # dp[i] is max profit at time i
    # dp[i] = max(dp[i-1], loop(dp[i-timespan[j] + profit[j]]))     Loop j over all jobs ending at i. Or don't choose these jobs.
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        if not startTime or not endTime or not profit: return 0
        n=len(startTime)
        if len(endTime)!=n or len(profit)!=n: return 0
        end=max(endTime)

        cache={}
        for i in range(n):
            if endTime[i] in cache:
                cache[endTime[i]].append(i)
            else:
                cache[endTime[i]]=[i]

        dp=[0]*(end+1)
        for i in range(2,end+1):
            dp[i]=dp[i-1]
            if i in cache:
                for j in cache[i]:
                    dp[i]=max(dp[i], (dp[startTime[j]] + profit[j]))
        return dp[end]


import unittest

class TestSolution(unittest.TestCase):
    def testJobScheduling(self):
        s = Solution()
        self.assertEqual(s.jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]), 120)
        self.assertEqual(s.jobScheduling(startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]), 150)
        self.assertEqual(s.jobScheduling(startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]), 6)
        


if __name__ == '__main__':
    unittest.main()