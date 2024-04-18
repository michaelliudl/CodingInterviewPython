from typing import List
from bisect import bisect_right, bisect_left
from functools import lru_cache

class Solution:

    # 1. Sort by start, use DFS to find max results of picking or not picking current job.
    #    In picking current case, find next job that starts right after current job ends.
    #    Use bisect_left to find left most index in case of duplicates.
    #    Optimize with memoization

    # DFS with memoization, recursion stack is used as DP storage
    # Solution 1, Sort by start time, then find next job that starts immediately after current end.
    # Use bisect_left to find first index in case of duplicate
    def jobSchedulingDFS(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        jobs = sorted(zip(startTime, endTime, profit))
        sortedStart = [job[0] for job in jobs]

        @lru_cache                  # LRU cache same as using {i: dfs result for i}
        def dfs(i):
            if i == len(jobs):      # No profit after last job
                return 0
            # Choice 1, not picking job `i`
            prof1 = dfs(i + 1)
            curEnd = jobs[i][1]
            curProf = jobs[i][2]

            j = bisect_left(sortedStart, curEnd)   # Binary search in sorted start times for place to insert current end time.
            # `j` is next job can pick that starts after current job ends
            # Choice 2, picking job `i`
            prof2 = dfs(j) + curProf
            return max(prof1, prof2)

        return dfs(0)   # DFS from first job

    # 2. Sort by end, use DP array to track max result.
    #    Find previous job that ends right before current job starts.
    #    Use bisect_right to find right most index in case of duplicates.

    # Use DP Array
    # Solution 2, Sort by end time, then find previous job that ends immediately before current start.
    # Use bisect_right to find last index in case of duplicate
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        jobs = sorted(zip(startTime, endTime, profit), key=lambda job: job[1])
        sortedEnd = [job[1] for job in jobs]
        dp = [0] * (len(jobs) + 1)

        for i in range(1, len(jobs) + 1):
            curStart, _, curProf = jobs[i - 1]
            prevIndex = bisect_right(sortedEnd, curStart)
            dp[i] = max(dp[i - 1], dp[prevIndex] + curProf)
        
        return dp[-1]

    # Same as solution 2, with self implemented binary search.
    # Create job combination of start/end time and profit. Sort by end time
    # dp[i] is maximum profit to get up to job i (inclusive)
    # dp[i] = max(dp[i-1],                              dp[j] + profit[i])
    #             max profit not includijng job i       max profit including job i, j is last job that ends before start time of job i
    #                                                   find j using binary search
    def jobSchedulingDP(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

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

        if not startTime or not endTime or not profit: 
            return 0
        n = len(startTime)
        if len(endTime) != n or len(profit) != n: 
            return 0
        jobs = []
        for i in range(n):
            jobs.append((startTime[i], endTime[i], profit[i]))
        jobs.sort(key=(lambda job: job[1]))         # DP method, sort intervals by endTime
        dp = [0] * (n + 1)
        for i in range(1, n + 1):                   # Loop forward, for each job, use binary search to find first job ending before current job's start, since jobs are sort by end time
            _, _, curProfit = jobs[i-1]
            j = binary_search(jobIndex = i - 1)
            dp[i] = max(dp[i - 1], dp[j] + curProfit)
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

    def error(self):
        raise KeyError('There is no answer')

import unittest

class TestSolution(unittest.TestCase):
    def testJobScheduling(self):
        s = Solution()
        self.assertEqual(s.jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]), 120)
        self.assertEqual(s.jobScheduling(startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]), 150)
        self.assertEqual(s.jobScheduling(startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]), 6)
        
    def testError(self):
        s = Solution()
        with self.assertRaises(KeyError):
            s.error()


if __name__ == '__main__':
    unittest.main()