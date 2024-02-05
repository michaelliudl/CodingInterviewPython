from typing import List
from bisect import bisect_right

class Solution:

    def jobSchedulingGPT(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dp = [0] * (len(jobs) + 1)

        for i in range(1, len(jobs) + 1):
            start_time, _, current_profit = jobs[i - 1]
            prev_index = bisect_right([job[1] for job in jobs], start_time)  # Find the latest job that finishes before the start time of the current job
            dp[i] = max(dp[i - 1], dp[prev_index] + current_profit)

        return dp[-1]
    
    # Create job combination of start/end time and profit. Sort by end time
    # dp[i] is maximum profit to get up to job i (inclusive)
    # dp[i] = max(dp[i-1],                              dp[j] + profit[i])
    #             max profit not includijng job i       max profit including job i, j is last job that ends before start time of job i
    #                                                   find j using binary search
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        def binary_search(jobIndex):
            curStart, _, _ = jobs[jobIndex]
            low, high = 0, jobIndex+1
            while low < high:
                mid = low + (high - low) // 2
                _, end, _ = jobs[mid]
                if end > curStart:
                    high = mid
                else:
                    low = mid + 1
            return low

        if not startTime or not endTime or not profit: return 0
        n=len(startTime)
        if len(endTime)!=n or len(profit)!=n: return 0
        jobs=[]
        for i in range(n):
            jobs.append((startTime[i], endTime[i], profit[i]))
        jobs.sort(key=(lambda job: job[1]))
        dp=[0]*(n+1)
        for i in range(1,n+1):
            _, _, curProfit = jobs[i-1]
            j = binary_search(jobIndex=i-1)
            dp[i] = max(dp[i-1], dp[j] + curProfit)
        return dp[n]


    # Memory limit exceed when endtime is 10**9 
    # dp[i] is max profit at time i
    # dp[i] = max(dp[i-1], loop(dp[i-timespan[j] + profit[j]]))     Loop j over all jobs ending at i. Or don't choose these jobs.
    def jobScheduling1(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
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